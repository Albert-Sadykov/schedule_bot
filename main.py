from core.config import load_config
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, ContentType
from core.handlers.basic import start, get_day, get_result, get_year
from aiogram.filters import Command
from core.utils.statesdesk import StepsDesk

logging.basicConfig(level=logging.INFO)
config = load_config(".env")


async def main():

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.message.register(start, Command(commands=['start']))
    dp.message.register(get_day, StepsDesk.GET_YEAR)
    dp.message.register(get_result, StepsDesk.GET_DAY)
    # dp.message.register(get_year, StepsDesk.GET_RESULT)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())