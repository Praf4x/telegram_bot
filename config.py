import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery

TOKEN = "8052641464:AAHsedqFTBoMo-2fEIXMvQ6OUcDFqlvIgaU"
bot = Bot(token=TOKEN)
dp = Dispatcher()