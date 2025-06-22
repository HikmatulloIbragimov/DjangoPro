import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram.types import Message

TOKEN = "7824519668:AAHb4wzZ58mslG8bSMgtW3GdhEkZR01ef94"

router = Router()

@router.message()
async def echo(message: Message):
    await message.answer("✅ Render работает!")

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    # Параллельный aiohttp-сервер
    async def handle(request):
        return web.Response(text="✅ I'm alive")

    app = web.Application()
    app.router.add_get("/", handle)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, port=3000)
    await site.start()

    print("🚀 Бот и HTTP-сервер запущены")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
