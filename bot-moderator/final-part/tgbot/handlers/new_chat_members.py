from aiogram.types import Message, ChatType

from loader import dp


@dp.message_handler(content_types=['new_chat_members'], chat_type=[ChatType.GROUP, ChatType.SUPERGROUP])
async def on_user_joined(message: Message):
    await message.delete()
