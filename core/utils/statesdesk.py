from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class StepsDesk(StatesGroup):
    GET_YEAR = State()
    GET_DAY = State()
