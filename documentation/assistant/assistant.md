# Assistant class

The class ```Assistant```

## Members

| Name                | Description                       |
|---------------------|-----------------------------------|
| ```self.identity``` | The base of the assistant himself |
| ```self.thread```   | The the conversation thread       |

## Constructor

Configures the openai api key and initiates ```self.identity``` and ```self.thread```.

## Methods

### send_message

#### Description

Sends a message to the AI assistant.

#### Arguments

| Name    | Type | Description                             |
|---------|------|-----------------------------------------|
| message | str  | The message to send to the AI assistant |

#### Returns
The thread message.

### run_thread
#### Description
Creates a run in the current thread.
