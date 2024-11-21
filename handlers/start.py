from aiogram import types, Dispatcher
from add_user import add_user
from utils.generate_code import generate_code

async def start_command(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or "No Username"

    # Проверяем, есть ли пользователь в таблице
    existing_code = add_user(user_id)
    if existing_code:
        await message.answer(f"Ваш код уже существует: {existing_code}")
        return

    # Генерируем новый код и сохраняем в Google Sheets
    code = generate_code()
    add_user(user_id, username, code)
    await message.answer(f"Ваш код: {code}")

def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
