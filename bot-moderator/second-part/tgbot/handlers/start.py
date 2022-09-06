from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def start_command(message: Message) -> Message:
    return await message.answer('Add a bot to the chat, give the administrator permissions and use it')
