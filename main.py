import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from aiogram import Bot, Dispatcher, types
from config import bot, dp, admin
from aiogram.utils import executor
from aiogram.types import ParseMode



# async def on_startup(_):
#     for i in admin:
#         await bot.send_message(chat_id=i, text="Бот включен!")
#         await db_main.sql_create()




# Добавление пользователя в таблицу
def add_user_to_sheet(user_id, username, code):
    sheet.append_row([user_id, username, code])

# Обработчик команды /start
async def start_command(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username or "No Username"

    # Проверяем наличие пользователя в таблице
    existing_code = check_user_in_sheet(user_id)
    if existing_code:
        await message.answer(f"Ваш уникальный код уже существует: {existing_code}")
        return

    # Генерируем новый код и добавляем в таблицу
async def generate_code(message: types.Message):
    code = generate_code()
    add_user_to_sheet(user_id, username, code)
    await message.answer(f"Ваш код: {code}")


# Основная функция запуска
if __name__ == '__main__':
    print("Бот включен!")
    executor.start_polling(dp, skip_updates=True)


# echo.register_echo(dp)

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO)
#     executor.start_polling(dp, skip_updates=True, on_startup=on_startup)