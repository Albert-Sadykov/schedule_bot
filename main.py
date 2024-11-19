from core.config import load_config
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, ContentType
from core.handlers.basic import start, get_photo
from aiogram.filters import Command


logging.basicConfig(level=logging.INFO)
config = load_config(".env")


async def main():

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.message.register(get_photo, F.photo)
    dp.message.register(start, Command(commands=['start']))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())