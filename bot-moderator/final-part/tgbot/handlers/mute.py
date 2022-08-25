from aiogram.types import Message, chat_permissions, ChatType

from datetime import timedelta

from loader import dp


@dp.message_handler(is_admin=True, commands=['mute'], commands_prefix='!/',
                    chat_type=[ChatType.GROUP, ChatType.SUPERGROUP])
async def mute_user(message: Message):
    if not message.reply_to_message:
        return await message.reply('This command need to be as reply on message')
    await message.delete()

    user_id = message.reply_to_message.from_user.id
    seconds = 30

    await message.bot.restrict_chat_member(chat_id=message.chat.id, user_id=user_id,
                                           until_date=timedelta(seconds=seconds),
                                           permissions=chat_permissions.ChatPermissions(can_send_messages=False,
                                                                                        can_send_polls=False,
                                                                                        can_send_other_messages=False,
                                                                                        can_send_media_messages=False))
    return await message.reply_to_message.reply(f'User has been muted for the {seconds} seconds')


@dp.message_handler(is_admin=True, commands=['unmute'], commands_prefix='!/',
                    chat_type=[ChatType.GROUP, ChatType.SUPERGROUP])
async def unmute_user(message: Message):
    if not message.reply_to_message:
        return await message.reply('This command need to be as reply on message')
    await message.delete()

    user_id = message.reply_to_message.from_user.id
    await message.bot.restrict_chat_member(chat_id=message.chat.id, user_id=user_id,
                                           permissions=chat_permissions.ChatPermissions(can_send_messages=True,
                                                                                        can_send_polls=True,
                                                                                        can_send_other_messages=True,
                                                                                        can_send_media_messages=True))
    return await message.reply_to_message.reply('User has been unmuted')
