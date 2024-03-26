import asyncio
import os

import discord
from aiogram import Bot, Dispatcher
from discord.ext import commands


class BaseChatTransport:
    def __init__(self, token):
        if not token or not isinstance(token, str):
            raise ValueError("Token must be a non-empty string")
        self.token = token

    def add_handler(event):
        raise RuntimeError("Not implemented")

    async def send_message(msg):
        raise RuntimeError("Not implemented")

    async def run(self):
        raise RuntimeError("Not implemented")


class ChatTransportDiscord(BaseChatTransport):
    def __init__(self, token):
        super().__init__(token)
        self.client = discord.Client()

    async def send_message(self, text, channel_id):
        channel = self.client.get_channel(channel_id)
        await channel.send(text)

    async def echo_handler(message) -> None:
        await message.channel.send(f"Hi! Your message was received: {message.content}")

    async def run(self):
        self.client.event(self.echo_handler)
        await self.client.run(self.token)


class ChatTransportTelegram(BaseChatTransport):
    def __init__(self, token):
        super().__init__(token)
        self.bot = Bot(token=self.token)
        self.dp = Dispatcher(self.bot)

    async def echo_handler(message) -> None:
        await message.answer(f"Hi! Your message was received: {message.text}")

    async def send_message(self, text, chat_id):
        await self.bot.send_message(text, chat_id=chat_id)

    async def run(self):
        self.dp.register_message_handler(self.echo_handler, state=None)
        await self.dp.start_polling(self.bot)
