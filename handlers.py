from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile

from data import (
    SERVICE_BUTTONS, PROMOCODES, service_links,
    service_emojis, IMAGE_PATHS, details_messages
)

router = Router()

# /start кнопки
@router.message(CommandStart())
async def start_handler(message: types.Message):
    keyboard = [[types.KeyboardButton(text=btn) for btn in row] for row in SERVICE_BUTTONS]
    await message.answer("Salom! Qaysi xizmat kerak?", reply_markup=types.ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    ))

# Детали (чат, ёрдам и т.п.)
@router.message(lambda msg: msg.text in details_messages)
async def info_handler(message: types.Message):
    await message.answer(details_messages[message.text])

# Основной обработчик кнопок
@router.message(lambda msg: any(service in msg.text for service in sum(SERVICE_BUTTONS, [])))
async def service_handler(message: types.Message):
    service = message.text.strip()
    emoji = service_emojis.get(service, "🎁")

    # Промокод
    clean_service = service.replace("🎁", "").replace("🍔", "").replace("🚀", "").strip()
    promo = PROMOCODES.get(clean_service)

    if promo:
        text = (
            f"<b>{emoji} {clean_service}</b>\n\n"
            f"✅ {promo['code']} - {promo['desc']} \n\n"
            f"@Promokodlar_24"
        )
    else:
        text = "<b>ZAFAR</b> - Ushbu promokod orqali 50% gacha chegirma olishingiz mumkin \n\n@Promokodlar_24"

    # Кнопки ссылок
    links = service_links.get(service, {})
    buttons = [[InlineKeyboardButton(text=k, url=v)] for k, v in links.items()]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons) if buttons else None

    # Картинка
    image_path = IMAGE_PATHS.get(service)
    if image_path:
        await message.answer_photo(photo=FSInputFile(image_path), caption=text, reply_markup=markup)
    else:
        await message.answer(text, reply_markup=markup)
