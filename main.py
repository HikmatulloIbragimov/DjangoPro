from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN = "7824519668:AAHb4wzZ58mslG8bSMgtW3GdhEkZR01ef94"  # вставь свой токен сюда

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

@dp.message()
async def handle_message(message: types.Message):
    await message.answer("Привет! Я работаю через Webhook 😎")
