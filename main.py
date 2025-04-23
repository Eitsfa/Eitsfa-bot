from config import *
from handlers import *
from aiogram import executor
from database import init_db

if __name__ == '__main__':
    init_db()
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)