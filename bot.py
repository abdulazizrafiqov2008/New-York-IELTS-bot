from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "New York LC Bot ga xush kelibsiz.\n"
        "Tez orada sizdan ism, telefon va IELTS darajangizni so'raymiz."
    )

async def main():
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
