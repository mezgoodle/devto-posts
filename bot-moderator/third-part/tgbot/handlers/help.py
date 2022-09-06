from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def help_command(message: Message) -> Message:
    """
    This handler will be called when a user sends `/help` command
    """
    return await message.answer("""
User's command:
    /help - get commands
    /admins - get chat admins
    /dice - roll a dice
Administrator's command:
    !kick - kick a user
    !ban - ban a user
    !mute - mute a user
    !unmute, !unban - opposite commands
""")
