import asyncio
from service.utils import SimpleBusinessLogicBot
from service.chat_transports import ChatTransportTelegram


async def main():
    transport_type = ChatTransportTelegram(token="TOKEN_HERE")
    simple_controler = SimpleBusinessLogicBot(transport_type=transport_type)
    simple_controler.run()


asyncio.run(main())
