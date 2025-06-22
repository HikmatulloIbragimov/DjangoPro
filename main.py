import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN = os.getenv("7824519668:AAHb4wzZ58mslG8bSMgtW3GdhEkZR01ef94")  # Используем переменную окружения

router = Router()

@router.message()
async def echo(message: Message):
    await message.answer("✅ Render работает!")

async def start_bot():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot)

async def start_web():
    async def handler(request):
        return web.Response(text="✅ I'm alive")

    app = web.Application()
    app.router.add_get("/", handler)
    runner = web.AppRunner(app)
    await runner.setup()

    # ВАЖНО: использовать порт из окружения
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, port=port)
    await site.start()

async def main():
    await asyncio.gather(start_bot(), start_web())

if __name__ == "__main__":
    asyncio.run(main())
