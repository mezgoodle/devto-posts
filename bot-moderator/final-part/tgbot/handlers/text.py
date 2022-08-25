from aiogram.types import Message, ChatType
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(state='waiting_for_answer', chat_type=[ChatType.GROUP, ChatType.SUPERGROUP])
async def on_user_answer(message: Message, state: FSMContext) -> Message:
    print(message.text)
    expected_result = (await state.get_data())['result']
    if message.text.isdigit() and int(message.text) == expected_result:
        await state.finish()
        return await message.answer('You are right!')
    else:
        await state.finish()
        return await message.answer('You are wrong!')
