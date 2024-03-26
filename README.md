# Test_task_Michael_Terner


General Recommendations

- Approach this as a real-world task at your job.
- There might be unclear aspects in the task description; feel free to ask clarifying questions.
- It's required to write basic tests (comprehensive coverage is not necessary – keep it very basic).
- Aim to complete and submit the task as quickly as possible, and manage the submission process independently.

---

1) Abstract Chat Transport Connector

The goal is to enable the bot to connect to any channel by simply swapping the transport class between Discord and Telegram, without altering the business logic.

Tasks to Implement:

- ChatTransport class
- def add_handler(event)
- async def send_message(msg)
- async def run
- ChatTransportDiscord service
- ChatTransportTelegram service
- SimpleBusinessLogic Bot
- Initializes ChatTransport (configured to work with either Discord or Telegram through a single setting).
- Listens for messages and responds with "Hi! Your message was received: {msg}".

The objective is to facilitate the bot's ability to receive and send messages from these two chat services. (You can request GPT-4 to write the code for this implementation).

---

Here's your text translated into English with enhancements for clarity and formatting:

---
