from pathlib import Path

# Папка с изображениями
BASE_IMAGE_PATH = Path("images")

# Кнопки (в порядке, заданном тобой)
SERVICE_BUTTONS = [
    ["🎁 Uzum Market", "🛍 Yandex Market"],
    ["🍔 Uzum Tezkor", "🌭 Yandex Eats"],
    ["🍕 Apex Pizza", "🍕Bellissimo Pizza"],
    ["🛸 Exprees24", "🥦 Yandex Магазин"],
    ["🚙 Wolt", "🛵 Yandex Dostavka"],
    ["🚀 Oqtepa Lavash Bot", "🩵 Yandex Lavka"],
    ["🚕 Uklon", "🎧 Yandex Plus"],
    ["🔶 Uzum Nasiya", "🛴 Jet"],
    ["💬 Chat {Muhokama}"],
    ["☎️ Yordam", "📭 Umumiy ma'lumotlar"]
]

# Промокоды (дефолт "ZAFAR" если не указано)
PROMOCODES = {
    "Uzum Market": {
        "code": "BORMISIZ",
        "desc": "180,000 soʻmdan yuqori bir marta ixtiyoriy xarid uchun -10,000 soʻm chegirma"
    },
    "Oqtepa Lavash Bot": {
        "code": "ZAFAR30",
        "desc": "95.000 mingdan oshgan buyrtma uchun 30.000 soʻm chegirma"
    },
    "Yandex Plus": {
        "code": "2TYKBV65MU",
        "desc": "1- oy davomida tekin musiqa dostvka va kino koʻrasiz"
    },
    "Yandex Market": {
        "code": "ZAFAR55",
        "desc": "Chegirma kod Yandex Market uchun"
    },
    "Uzum Tezkor": {
        "code": "ZAFAR",
        "desc": "65.000 soʻmdan  oshgan buyrtma uchun 21.000 soʻmdan 3 marta chegirma"
    },
    "Yandex Eats": {
        "code": "UKBMX",
        "desc": "80.000 oshgan buyrtma uchun 30 ming soʻm chegirma"
    },
    "Express24": {
        "code": "STRK7",
        "desc": "80.000 oshgan burtma uchun 30 ming soʻm chegirma"
    },
    "Bellissimo Pizza": {
        "code": "ZAFAR30",
        "desc": "Bellissimo Pizzada 30% chegirma"
    },
    "Apex Pizza": {
        "code": "ZAFAR",
        "desc": "Apex Pizzada maxsus promokod"
    },
    "Yandex Dostavka": {
        "code": "ZAFAR",
        "desc": "Yetkazib berish uchun promokod"
    },
    "Yandex Lavka": {
        "code": "TOSHKENT51",
        "desc": "Birinchi buyrtma uchun 50% chegirma , ushbu xavola orqali o`tishingiz mumkin \n\n 👇https://lavka.prfl.me/youtube/48x0e5"
    },
    "Yandex Магазин": {
        "code": "ZAFAR",
        "desc": "Yandex do'koni uchun promokod"
    },
    "Jet": {
        "code": "7HMKOQ",
        "desc": "20 daqiqa bepul samakat uchasiz"
    },
    "Uzum Nasiya": {
        "code": "NASIYA90",
        "desc": "1,400,000 soʻmdan yuqori Nasiyaga xarid uchun -90,000 soʻm chegirma"
    },
    "Wolt": {
        "code": "B3HF5N7",
        "desc": "80 mingdan oshgan buyurtmalar uchun 15 ming soʻmdan 3 marta chegirma"
    },
    "Uklon": {
        "code": "ZAFAR",
        "desc": "Uklon uchun promokod"
    }
}


# Эмодзи
service_emojis = {
    "🎁 Uzum Market": "🛍",
    "🛍 Yandex Market": "🛍",
    "🍔 Uzum Tezkor": "🍔",
    "🌭 Yandex Eats": "🌭",
    "🍕 Apex Pizza": "🍕",
    "🍕Bellissimo Pizza": "🍕",
    "🛸 Exprees24": "🛸",
    "🥦 Yandex Магазин": "🥦",
    "🚙 Wolt": "🚙",
    "🛵 Yandex Dostavka": "🛵",
    "🚀 Oqtepa Lavash Bot": "🚀",
    "🩵 Yandex Lavka": "🩵",
    "🚕 Uklon": "🚕",
    "🎧 Yandex Plus": "🎧",
    "🔶 Uzum Nasiya": "🔶",
    "🛴 Jet": "🛴",
}

# Изображения
IMAGE_PATHS = {}

photo_index = 1

for row in SERVICE_BUTTONS:
    for name in row:
        if name == "🛍 Yandex Market":
            IMAGE_PATHS[name] = str(BASE_IMAGE_PATH / "yandex_market.jpg")
        elif name == "🥦 Yandex Магазин":
            IMAGE_PATHS[name] = str(BASE_IMAGE_PATH / "2_photo.jpg")
        else:
            IMAGE_PATHS[name] = str(BASE_IMAGE_PATH / f"{photo_index}_photo.jpg")
        photo_index += 1  # ✅ Всегда увеличиваем!
# Ссылки
service_links = {
    "🍔 Uzum Tezkor": {"📥 Ilovaga kirish": "https://www.uzum.uz/"},
    "🎁 Uzum Market": {"📥 Ilovaga kirish": "https://uzum.uz/"},
    "🛍 Yandex Market": {"📥 Kirish": "https://market.yandex.ru/"},
    "🌭 Yandex Eats": {"📥 Ilovaga kirish": "https://go.yandex/"},
    "🚀 Oqtepa Lavash Bot": {"📢 Aksiyalar": "https://t.me/promokod_zafar"},
    "🛸 Exprees24": {"📥 Ilovaga kirish": "https://express24.uz"},
    "🎧 Yandex Plus": {"✅ Obuna boʻlish": "https://ypls-eats.prfl.me/promokod"},
}

# Информация (чат, помощь)
details_messages = {
    "💬 Chat {Muhokama}": "💬 Chegirma va promokodlar muhokama qilinadi:\n\nhttps://t.me/+5RBCdNMPms5iNzBi",
    "☎️ Yordam": "😊 Assalomu alaykum! \n Ushbu nomerga bog`lanib yordamga ega bo`lishingiz mumkin!!!\n\n📞 +998-94-970-00-57",
    "📭 Umumiy ma'lumotlar": "📢 Telegram kanalimiz:\n\n🛒 https://t.me/promokod_zafar"
}
