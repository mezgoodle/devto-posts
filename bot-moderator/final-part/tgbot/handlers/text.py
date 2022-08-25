from aiogram import Bot
from aiogram.types import Message, ChatType
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(state='waiting_for_answer', chat_type=[ChatType.GROUP, ChatType.SUPERGROUP])
async def on_user_answer(message: Message, state: FSMContext) -> Message:
    state_data = await state.get_data()
    bot: Bot = message.bot
    await bot.delete_message(message.chat.id, state_data['message_id'])
    await message.delete()
    await state.finish()
    if not message.text.isdigit() and int(message.text) != state_data['result']:
        # delete from the chat
        return await message.answer('You are wrong!')
