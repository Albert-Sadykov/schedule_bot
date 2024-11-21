from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def create_year_markup():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=f'{year} курс'), KeyboardButton(text=f'{year + 1} курс')]  for year in range(1, 6, 2)
        ], 

    )
    
    return markup

def create_day_markup(course):
    course = course[0]
    if course == '1':
        markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Понедельник'), KeyboardButton(text='Вторник')],
            [KeyboardButton(text='Среда'), KeyboardButton(text='Четверг')],
            [KeyboardButton(text='Пятница'), KeyboardButton(text='Суббота')]

        ],
        resize_keyboard=True,
        one_time_keyboard=True
        )
    elif course == "2":
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='Понедельник'), KeyboardButton(text='Вторник')],
                [KeyboardButton(text='Среда'), KeyboardButton(text='Четверг')],
                [KeyboardButton(text='Пятница')]

            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    elif course == "3":
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='Понедельник'), KeyboardButton(text='Среда')],
                [KeyboardButton(text='Четверг'), KeyboardButton(text='Пятница')]

            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    elif course == "4":
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='Понедельник'), KeyboardButton(text='Вторник')],
                [KeyboardButton(text='Среда'), KeyboardButton(text='Пятница')]

            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    elif course == '5':
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='Понедельник'), KeyboardButton(text='Вторник')],
                [KeyboardButton(text='Четверг'), KeyboardButton(text='Пятница')]

            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    elif course == '6':
        markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Понедельник'), KeyboardButton(text='Вторник')],
            [KeyboardButton(text='Среда'), KeyboardButton(text='Четверг')],
            [KeyboardButton(text='Суббота')]

        ],
        resize_keyboard=True,
        one_time_keyboard=True
        )
    
    return markup

