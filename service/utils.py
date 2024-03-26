import asyncio
from .chat_transports import BaseChatTransport


class SimpleBusinessLogicBot:
    def __init__(self, chat_transport):
        if isinstance(chat_transport, BaseChatTransport):
            self.transport = chat_transport

    async def run(self):
        await self.transport.run()
