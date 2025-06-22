from flask import Flask, request
import asyncio

from bot import bot, dp

app = Flask(__name__)
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = "https://your-app-name.onrender.com" + WEBHOOK_PATH  # ЗАМЕНИ на свой Render URL

@app.route("/")
def index():
    return "✅ Бот работает!"

@app.route(WEBHOOK_PATH, methods=["POST"])
async def webhook():
    update = await request.get_data()
    await dp.feed_raw_update(bot, update)
    return "ok"

async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(on_startup())
    app.run(host="0.0.0.0", port=5000)
