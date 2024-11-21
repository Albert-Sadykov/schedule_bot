from aiogram import Bot, types
from aiogram.types import Message
from core.keyboards.reply import create_year_markup, create_day_markup
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from core.utils.statesdesk import StepsDesk
from core.utils.work_functions import is_even_week, show_schedule
from core.utils.schedule import schedule
from aiogram.enums.parse_mode import ParseMode

global student_answer
student_answer = {
    "course": None,
    "day": None
}

async def start(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(message.chat.id, 'Расписание учебных занятий кафедры теоретических основ разработки месторождений нефти и газа геологического факультета МГУ', reply_markup=create_year_markup())
    await state.set_state(StepsDesk.GET_YEAR)

async def get_day(message: Message, bot: Bot, state: FSMContext):
    global student_answer
    student_answer["course"] = message.text
    await bot.send_message(message.chat.id, "Выберете день недели", reply_markup=create_day_markup(student_answer["course"]))
    await state.set_state(StepsDesk.GET_DAY)

async def get_result(message: Message, bot: Bot, state: FSMContext):
    global student_answer
    student_answer["day"] = message.text
    desk = schedule[student_answer["course"]][is_even_week()][student_answer["day"]]
    
    print(desk)
    await bot.send_message(message.chat.id, show_schedule(student_answer["day"], desk), reply_markup=create_year_markup(), parse_mode=ParseMode.HTML)

    await get_year(message, bot, state)

async def get_year(message: Message, bot: Bot, state: FSMContext):
    global student_answer
    await state.set_state(StepsDesk.GET_YEAR)
