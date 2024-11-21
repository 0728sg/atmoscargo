from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
GOOGLE_SHEET_NAME = "Client Codes"
CREDENTIALS_FILE = "credentials.json"

admin = [5649689334, ]