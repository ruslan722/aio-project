from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ..models import User

MARKS = {
    True: '✅',
    False: '❌',
    None: '✏️',
}

async def kb_week_menu(user: User):
   
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text='Д.Нед',
                callback_data='week_day_header',
            ),
            InlineKeyboardButton(
                text='Раб.вр',
                callback_data='work_time_header',
            ),
            InlineKeyboardButton(
                text='Обед',
                callback_data='lunch_time_header',
            ),
            InlineKeyboardButton(
                text='Перер',
                callback_data='timeout_header',
            ),
        ]
    ]

    for schedule in user.schedule:
        print(f"{MARKS[schedule.enable]} {schedule.week_day}", f'schedule_{schedule.id}')
        inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text=f"{MARKS[schedule.enable]} {schedule.week_day}",
                    callback_data=f'schedule_{schedule.id}',
                ),
                InlineKeyboardButton(
                    text='.',
                    callback_data='.'
                ),
                InlineKeyboardButton(
                    text='.',
                    callback_data='.'
                ),
                InlineKeyboardButton(
                    text='.',
                    callback_data='.'
                ),
            ]
        )

    return InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard
    )
    