import asyncio
import aioschedule

from loader import bot
from aiogram.types import BotCommand
from aiogram.utils.exceptions import ChatNotFound
from config import ADMIN_ID


async def on_startup(dp):
    pass


async def on_shutdown(dp):
    pass


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
