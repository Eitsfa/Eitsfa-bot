from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, ADMINS, CHANNELS

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(msg: types.Message):
    keyboard = InlineKeyboardMarkup()
    for ch in CHANNELS:
        keyboard.add(InlineKeyboardButton(text=f"عضویت در {ch}", url=f"https://t.me/{ch[1:]}"))
    keyboard.add(InlineKeyboardButton(text="ادامه", callback_data="check_subs"))
    await msg.answer(f"سلام {msg.from_user.full_name} عزیز، به ربات ایتسفا خوش آمدید!", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == "check_subs")
async def check_subs(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    for ch in CHANNELS:
        member = await bot.get_chat_member(chat_id=ch, user_id=user_id)
        if member.status not in ['member', 'administrator', 'creator']:
            await callback.answer("لطفاً در کانال‌ها عضو شوید.", show_alert=True)
            return
    await callback.message.answer("اکنون می‌توانید از ربات استفاده کنید.")