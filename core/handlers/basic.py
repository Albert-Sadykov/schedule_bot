from aiogram import Bot
from aiogram.types import Message

async def start(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, 'Привет! Это бот для управления VPN.')

async def get_photo(message: Message, bot: Bot):
    await message.answer("Thanks")
