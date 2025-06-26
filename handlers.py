from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile

from data import (
    SERVICE_BUTTONS, PROMOCODES, service_links,
    service_emojis, IMAGE_PATHS, details_messages
)

router = Router()

# Стартовое меню
@router.message(CommandStart())
async def start_handler(message: types.Message):
    keyboard = [[types.KeyboardButton(text=btn) for btn in row] for row in SERVICE_BUTTONS]
    await message.answer("Salom! Qaysi xizmat kerak?", reply_markup=types.ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    ))

# Статические сообщения (Ёрдам, Маълумотлар и т.п.)
@router.message(lambda msg: msg.text in details_messages)
async def info_handler(message: types.Message):
    await message.answer(details_messages[message.text])

# Обработка всех сервисов
@router.message(lambda msg: any(msg.text == btn for btn in sum(SERVICE_BUTTONS, [])))
async def service_handler(message: types.Message):
    service = message.text.strip()
    emoji = service_emojis.get(service, "🎁")

    # Убираем эмодзи для PROMOCODES
    clean_service = service
    for char in emoji:
        clean_service = clean_service.replace(char, "")
    clean_service = clean_service.strip()

    promo = PROMOCODES.get(clean_service)

    if promo:
        text = (
            f"<b>{emoji} {clean_service}</b>\n\n"
            f"✅ <b>{promo['code']}</b> - {promo['desc']}\n\n"
            f"@promokod_zafar"
        )
    else:
        text = (
            f"<b>{emoji} {clean_service}</b>\n\n"
            f"✅ <b>ZAFAR</b> - Ushbu promokod orqali 50% gacha chegirma olishingiz mumkin\n\n"
            f"@promokod_zafar"
        )

    # Кнопки ссылок
    links = service_links.get(service, {})
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=text, url=url)] for text, url in links.items()
    ]) if links else None

    # Картинка (если есть)
    image_path = IMAGE_PATHS.get(service)
    if image_path:
        await message.answer_photo(photo=FSInputFile(image_path), caption=text, reply_markup=markup)
    else:
        await message.answer(text, reply_markup=markup)
