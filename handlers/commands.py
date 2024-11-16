from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
import os
from buttons import start
from config import bot

async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=
        'Я бот, который генерирует уникальные коды для клиентов.\n'
        'Доступные команды:\n'
        '/start — получить код\n' )
    await message.answer(text=
        'Я бот, который генерирует уникальные коды для клиентов.\n'
        'Доступные команды:\n'
        '/start — получить код\n' )



def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])