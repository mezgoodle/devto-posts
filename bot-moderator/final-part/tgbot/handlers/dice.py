from aiogram.types import Message

from loader import dp


@dp.message_handler(commands=['dice'])
async def role_dice(message: Message) -> Message:
    return await message.answer_dice()
