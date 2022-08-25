from aiogram.types import Message, ChatType
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hbold

from loader import dp

from random import randint


@dp.message_handler(content_types=['new_chat_members'], chat_type=[ChatType.GROUP, ChatType.SUPERGROUP])
async def on_user_joined(message: Message, state: FSMContext) -> Message:
    new_member = message.new_chat_members[0]
    first_number, second_number = randint(1, 10), randint(1, 10)
    result = first_number + second_number
    await state.update_data(result=result, new_member_id=new_member.id)
    await state.set_state('waiting_for_answer')
    await message.delete()
    return await message.answer(f"Welcome, {new_member.full_name}! Solve this mathematical expression: {hbold(first_number)} + {hbold(second_number)}. You only have one attempt")
