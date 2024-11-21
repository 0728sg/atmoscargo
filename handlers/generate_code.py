import types
from handlers.add_user import add_user_to_sheet
import random


async def generate_code(message: types.Message, user_id=None, username=None):
    code = generate_code()
    add_user_to_sheet(user_id, username, code)
    await message.answer(f"Ваш код: {code}")


# Функция генерации уникального кода
def generate_code():
    return f"CODE-{random.randint(1000, 9999)}"
