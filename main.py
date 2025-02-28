import asyncio
import logging
import os
from pathlib import Path
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from config import TOKEN  # Убедитесь, что у вас есть файл config.py с переменной TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Функция для проверки наличия файла
def get_photo_path(filename):
    photo_path = Path(__file__).parent / "photos" / filename
    if not photo_path.exists():
        print(f"Ошибка: Файл {photo_path} не найден!")
        return None
    return types.FSInputFile(photo_path)

async def mainmenu(msg: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Заказы")],
            [KeyboardButton(text="Личный кабинет 📂")],
            [KeyboardButton(text="Информация ℹ️"), KeyboardButton(text="Тех.поддержка 🌐")]
        ],
        resize_keyboard=True
    )
    await msg.answer("Главное меню", reply_markup=keyboard)

@dp.message(Command("start"))
async def start(msg: types.Message):
    keyboard1 = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="rus")],
            [KeyboardButton(text="eng")]
        ],
        resize_keyboard=True
    )
    await msg.answer("Выберите язык/lang", reply_markup=keyboard1)

@dp.message()
async def handle_callback_query(msg: types.Message):
    if msg.text == "Тех.поддержка 🌐":
        photo = get_photo_path("mainmenu.jpg")
        text = """
Правила обращения в Техническую Поддержку:

🔹 1. <b>Представьтесь, изложите проблему своими словами - мы постараемся Вам помочь.</b>
🔹 2. <b>Напишите свой ID</b> - нам это нужно, чтобы увидеть ваш профиль.
🔹 3. <b>Будьте вежливы</b>, наши консультанты не роботы.

<i>Напишите нам, ответ Поддержки не заставит вас долго ждать!</i>
        """
        inline_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Поддержка", url="https://t.me/support")]
            ]
        )
        if photo:
            await msg.answer_photo(photo=photo, caption=text, parse_mode="HTML", reply_markup=inline_keyboard)
        else:
            await msg.answer("Ошибка: изображение отсутствует", parse_mode="HTML")

    elif msg.text == "Информация ℹ️":
        photo = get_photo_path("information.jpg")
        text = """
О Сервисе

<i>Наш сервис</i> <b>— торговая площадка для NFT. Покупайте, продавайте и открывайте для себя эксклюзивные цифровые предметы.</b>
        """
        inline1_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Соглашение", url="https://t.me/terms"),
                 InlineKeyboardButton(text="Поддержка", url="https://t.me/support")],
                [InlineKeyboardButton(text="Сообщить об ошибке", url="https://t.me/report")]
            ]
        )
        if photo:
            await msg.answer_photo(photo=photo, caption=text, parse_mode="HTML", reply_markup=inline1_keyboard)
        else:
            await msg.answer("Ошибка: изображение отсутствует", parse_mode="HTML")

    elif msg.text == "Личный кабинет 📂":
        text = """
<b>Личный кабинет</b>

Баланс: N₽
Заморожено: N₽
Верификация: ⚠️ <b>Не верифицирован / ✅ Верифицирован</b>
Ваш ID: ID пользователя
Имя пользователя: Name
<b>Возраст: N лет</b>
<b>В сервисе: N дней</b>
Выполненных заказов: N
Рейтинг: <b>N/10</b>
        """
        inline_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Мои отзывы", callback_data="otz")],
                [InlineKeyboardButton(text="Активные заказы", callback_data="act"),
                 InlineKeyboardButton(text="Отмененные заказы", callback_data="no"),
                 InlineKeyboardButton(text="Завершенные заказы", callback_data="end")],
                [InlineKeyboardButton(text="Пополнить", callback_data="dep"),
                 InlineKeyboardButton(text="Вывести", callback_data="undep")]
            ]
        )
        await msg.answer(text, parse_mode="HTML", reply_markup=inline_keyboard)

    elif msg.text == "eng":
        await msg.answer("Вы выбрали English.")

    elif msg.text == "rus":
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Заказчик")],
                [KeyboardButton(text="Специалист")]
            ],
            resize_keyboard=True
        )
        await msg.answer("Вы выбрали Русский. Кто вы?", reply_markup=keyboard)

    elif msg.text == "Заказчик":
        keyboard1 = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="вернуться назад")]],
            resize_keyboard=True
        )
        await msg.answer("Тут есть вопрос.", reply_markup=keyboard1)

    elif msg.text == "вернуться назад":
        await mainmenu(msg)

    elif msg.text == "Специалист":
        keyboard = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="вернуться назад")]],
            resize_keyboard=True
        )
        await msg.answer("Введите ваше имя")
        await msg.answer("Введите Вашу дату рождения")
        await msg.answer("После этого нажмите кнопку ниже", reply_markup=keyboard)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
