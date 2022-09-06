from aiogram.types import Message, ChatType

from loader import dp


@dp.message_handler(commands=['admins'], chat_type=[ChatType.GROUP, ChatType.SUPERGROUP])
async def admins_command(message: Message) -> Message:
    chat_id = message.chat.id
    admins = await message.bot.get_chat_administrators(chat_id)
    text = ''
    for admin in admins:
        text += f'@{admin.user.username} '
    return await message.answer(text, disable_notification=True)
