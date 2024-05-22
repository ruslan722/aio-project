from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from ..keyboards.start import COMMANDS
from ..models import User, Schedule

router = Router()


@router.message(Command('start'))
async def start_command(message: Message, state: FSMContext):
    await state.clear()
    await message.bot.set_my_commands(COMMANDS)


    user, created = User.get_or_create(telegram_id=message.from_user.id)
    if created:
        for week_day in ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']:
            Schedule.create(
                user=user,
                week_day=week_day,
            )