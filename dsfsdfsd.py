from config import *

async def mainmenu(msg: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Заказы")],
            [KeyboardButton(text="Личный кабинет 📂")],
            [KeyboardButton(text="Информация ℹ️"), KeyboardButton(text="Тех.поддержка 🌐", )]
        ],
        resize_keyboard=True

    )
    await msg.answer("Главное меню", reply_markup=keyboard)



async def info(msg: types.Message):
    photo = types.FSInputFile("photos/information.jpg")
    text="""
О Сервисе 

<i>Наш сервис</i> <b>— торговая площадка 
для невзаимозаменяемых 
токенов (NFT). Покупайте, 
продавайте и открывайте для 
себя эксклюзивные цифровые 
предметы.</b>
    """

    # Создание inline клавиатуры
    inline1_keyboard = InlineKeyboardMarkup(
                inline_keyboard=[
                [InlineKeyboardButton(text="Соглашение", url="https://copilot.microsoft.com/chats/kggchugg2RNgPiTYTmaMy"), InlineKeyboardButton(text="Поддержка", url="https://copilot.microsoft.com/chats/kggchugg2RNgPiTYTmaMy"),],
                [InlineKeyboardButton(text="Сообщить об ошибке", url="https://copilot.microsoft.com/chats/kggchugg2RNgPiTYTmaMy")]

            ]
        )
    await msg.answer_photo(caption=text, parse_mode="HTML",photo=photo,reply_markup=inline1_keyboard) 

