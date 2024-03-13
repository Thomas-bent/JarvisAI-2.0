import json
import time

import openai
from openai.pagination import SyncCursorPage
from openai.types.beta.threads import RequiredActionFunctionToolCall, Run

from function_names import FunctionNames
from roles import Roles
from status import Status
from config_files import config
import functions


class Assistant:
    """
    Main class of the Ai assistant.
    """

    def __init__(self):
        openai.api_key = config.OPENAI_API_KEY
        self.identity = openai.beta.assistants.create(
            name=config.assistant.NAME,
            instructions=config.assistant.INSTRUCTIONS,
            tools=config.assistant.TOOLS,
            model=config.assistant.MODEL
        )
        self.thread = openai.beta.threads.create()

    def send_message(self, message: str):
        """
        Sends a message to the openai assistant API.
        :param message: The message to send.
        :return: The thread message.
        """
        return openai.beta.threads.messages.create(
            thread_id=self.thread.id,
            role=Roles.USER.value,
            content=message
        )

    def run_thread(self):
        """
        Creates a new run in the current thread.
        :return: The created run.
        """
        return openai.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.identity.id
        )

    def get_run(self, run: Run) -> Run:
        """
        Updates the run.
        :param run: The run that will be updated.
        :return: The updated run.
        """
        return openai.beta.threads.runs.retrieve(
            thread_id=self.thread.id,
            run_id=run.id
        )

    def get_messages(self) -> SyncCursorPage:
        """
        :return: All messages in the current thread.
        """
        return openai.beta.threads.messages.list(
            thread_id=self.thread.id
        )

    def message_and_response(self, message: str) -> str:
        """
        Sends a message to the openai assistants API.
        :param message: The message to send.
        :return: The API response message.
        """
        self.send_message(message)
        run = self.run_thread()
        while self.get_run(run).status != Status.COMPLETED:
            if self.get_run(run).status == Status.REQUIRES_ACTION:
                self.function_calling(run)
            time.sleep(config.assistant.TAKT)
        return self.get_messages().data[0].content[0].text.value

    def is_status(self, run: Run, status: str) -> bool:
        """
        Checks if the run has the given status.
        :param run: The run to check.
        :param status: The status in question.
        :return: If the status is the same.
        """
        return self.get_run(run).status == status

    def function_calling(self, run: Run) -> None:
        """
        Checks if action is required, if yes, calls functions and submits their outputs.
        :param run: The current run.
        """
        while self.is_status(run, Status.REQUIRES_ACTION.value):
            func_calls = self.get_run(run).required_action.submit_tool_outputs.tool_calls
            outputs = self.get_output_list(func_calls)
            self.submit_tool_outputs(run, outputs)

            while not self.get_run(run).status in [Status.QUEUED, Status.COMPLETED, Status.REQUIRES_ACTION]:
                time.sleep(config.assistant.TAKT)

    def submit_tool_outputs(self, run: Run, outputs: list[dict[str, str]]) -> None:
        """
        Submits the output of the function calls back to the openai API.
        :param run: The current run.
        :param outputs: The outputs of the function calls.
        """
        openai.beta.threads.runs.submit_tool_outputs(
            thread_id=self.thread.id,
            run_id=run.id,
            tool_outputs=outputs
        )

    def get_output_list(self, func_calls: list[RequiredActionFunctionToolCall]) -> list[dict[str, str]]:
        """
        Executes a list of function calls.
        :param func_calls: The list of function calls.
        :return: The output of the called functions.
        """
        outputs = []
        for call in func_calls:
            print(call.function.arguments)
            out = self.get_output(call.function.name, json.loads(call.function.arguments))
            outputs.append({
                "tool_call_id": call.id,
                "output": out
            })
        return outputs

    @staticmethod
    def get_output(function_name: str, args: dict) -> str:
        """
        Executes a function by its name.
        :param function_name: The name of the function.
        :param args: Function arguments.
        :return: Output of the function.
        """
        if function_name == FunctionNames.CAPTURE_IMAGE.value:
            return functions.capture_image(args['filename'])
        elif function_name == FunctionNames.CREATE_FILE.value:
            return functions.create_file(args['filename'], args['path'])
        elif function_name == FunctionNames.CREATE_FOLDER.value:
            return functions.create_folder(args['folder_name'], args['path'])
        elif function_name == FunctionNames.WRITE_FILE.value:
            return functions.write_file(args['filename'], args['content'], args['path'])
        elif function_name == FunctionNames.CONSOLE_COMMAND.value:
            return functions.console_command(args['command'])
        else:
            return f"The function '{ function_name }' was not found"
