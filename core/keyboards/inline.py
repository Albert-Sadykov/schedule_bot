from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def create_year_markup():
    btn = [[InlineKeyboardButton(text=f"{i} курс", callback_data=f"{i}") for i in range(1, 7)]]
    markup = InlineKeyboardMarkup(inline_keyboard=btn)
    
    return markup