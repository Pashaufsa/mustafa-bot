import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.getenv("BOT_TOKEN", "8742884938:AAGKgAc1xzmoJKzIsHtFt2G9V6xRged8iEI")

logging.basicConfig(level=logging.WARNING)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Главное меню
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❓ Как Мустафа?"),
            KeyboardButton(text="🌐 Соцсети Мустафы"),
        ],
        [
            KeyboardButton(text="📢 Каналы"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выбери пункт меню"
)

# Инлайн-кнопки с соцсетями
socials_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📸 Instagram",
                              url="https://www.instagram.com/twistikx?igsh=MTFxNGV4b3NuM2t0ZQ%3D%3D&utm_source=qr")],
        [InlineKeyboardButton(text="🎵 TikTok", url="https://www.tiktok.com/@twistikx1")],
        [InlineKeyboardButton(text="🔗 Blink", url="https://blinkmap.com/@twistikx")],
        [InlineKeyboardButton(text="💙 VK", url="https://vk.ru/m.andreevich1")],
    ]
)

# Инлайн-кнопки с каналами
channels_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="👤 Канал Мустафы", url="https://t.me/twistiktwik")],
        [InlineKeyboardButton(text="🔒 СИЗО", url="https://t.me/savoknaxyi")],
        [InlineKeyboardButton(text="🇦🇿 Азерчайцы", url="https://t.me/auenarukavekarandaw")],
    ]
)


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    user = message.from_user
    username = f"@{user.username}" if user.username else f"{user.full_name} (без юзернейма)"
    print(f"🟢 Новый пользователь запустил бота: {username} | ID: {user.id}")

    await message.answer(
        "Привет! 👋 Я бот о Мустафе.\nВыбери, что тебя интересует:",
        reply_markup=main_keyboard
    )


@dp.message(F.text == "❓ Как Мустафа?")
async def how_mustafa(message: types.Message):
    await message.answer(
        "❓ <b>Как Мустафа?</b>\n\n"
        "Мустафа чувствует себя отлично! 😄",
        parse_mode="HTML"
    )


@dp.message(F.text == "🌐 Соцсети Мустафы")
async def socials(message: types.Message):
    await message.answer(
        "🌐 <b>Соцсети Мустафы</b>\n\nВыбирай и подписывайся! 👇",
        parse_mode="HTML",
        reply_markup=socials_keyboard
    )


@dp.message(F.text == "📢 Каналы")
async def channels(message: types.Message):
    await message.answer(
        "📢 <b>Каналы</b>\n\nПодписывайся! 👇",
        parse_mode="HTML",
        reply_markup=channels_keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
