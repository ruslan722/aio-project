from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from ..keyboards.settings import kb_week_menu
from ..models import User, Schedule

router = Router()

@router.message(Command('settings'))
async def settings_command(message: Message):
    
    user = User.get(telegram_id=message.from_user.id)
    await message.answer(
        text='Настройки пользователя',
        reply_markup=await kb_week_menu(user),
    )

@router.callback_query(F.data.startswith('schedule_'))
async def schedule_id_handler(callback: CallbackQuery):
    schedule_id = int(callback.data.split('_')[-1])
    schedule: Schedule = Schedule.get_by_id(schedule_id)
    schedule.enable = not schedule.enable
    schedule.save()
    await callback.bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=await kb_week_menu(schedule.user),
    )