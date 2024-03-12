import json
import time

import openai
from assistant.roles import Roles
from assistant.status import Status
from config_files import config


class Assistant:
    """
    Main class of the Ai assistant.
    """

    def __init__(self):
        openai.api_key = config.OPENAI_API_KEY
        self.identity = openai.beta.assistants.create(
            name=config.assistant.name,
            instructions=config.assistant.instructions,
            tools=config.assistant.tools,
            model=config.assistant.model
        )
        self.thread = openai.beta.threads.create()

    def send_message(self, message: str):
        return openai.beta.threads.messages.create(
            thread_id=self.thread.id,
            role=Roles.USER,
            content=message
        )

    def run_thread(self):
        return openai.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.identity.id
        )

    def get_run(self, run):
        return openai.beta.threads.runs.retrieve(
            thread_id=self.thread.id,
            run_id=run.id
        )

    def get_messages(self):
        return openai.beta.threads.messages.list(
            thread_id=self.thread.id
        )

    def message_and_response(self, message: str):
        msg = self.send_message(message)
        run = self.run_thread()
        while self.get_run(run).status != Status.COMPLETED:
            if self.get_run(run).status == Status.REQUIRES_ACTION:
                self.function_calling(run)
            time.sleep(config.assistant.takt)
        return self.get_messages().data[0].content[0].text.value

    def is_status(self, run, status: str) -> bool:
        return self.get_run(run).status == status

    def function_calling(self, run):
        while self.is_status(run, Status.REQUIRES_ACTION):
            func_calls = self.get_run(run).required_action.submit_tool_outputs.tool_calls
            outputs = self.get_output_list(func_calls)
            self.submit_tool_outputs(run, outputs)

            while not self.get_run(run).status in ["queued", "completed", "requires_action"]:
                time.sleep(config.assistant.takt)

    def submit_tool_outputs(self, run, outputs):
        openai.beta.threads.runs.submit_tool_outputs(
            thread_id=self.thread.id,
            run_id=run.id,
            tool_outputs=outputs
        )

    def get_output_list(self, func_calls):
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
    def get_output(function_name, args):
        if function_name == "get_favourite_movie":
            print("inception")
        else:
            return "The function was not found"
