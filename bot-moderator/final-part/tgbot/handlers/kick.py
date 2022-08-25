from aiogram.types import Message, ChatType

from loader import dp

from datetime import timedelta


@dp.message_handler(is_admin=True, commands=['kick'], commands_prefix='!/',
                    chat_type=[ChatType.GROUP, ChatType.SUPERGROUP])
async def kick_user(message: Message):
    if not message.reply_to_message:
        return await message.reply('This command need to be as reply on message')
    await message.delete()

    user_id = message.reply_to_message.from_user.id
    seconds = 30
    await message.bot.ban_chat_member(chat_id=message.chat.id, user_id=user_id, until_date=timedelta(seconds=seconds))
    return await message.reply_to_message.reply(f'User has been kicked for the {seconds} seconds')
