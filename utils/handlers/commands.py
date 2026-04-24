import asyncio
from datetime import datetime
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, FSInputFile 
from aiogram import Router, F, types
from aiogram.filters import CommandStart

from utils.layouts.layout import main_admin_kb, main_user_kb
from presentation.create_bot import admins, bot

user_router = Router()
users_id = []

@user_router.message(CommandStart())
async def command_start(message: Message):
    web_app_url = 'https://github.com/Ratorgis/'
    open_app_button = InlineKeyboardButton(
        text = 'Open mini app',
        web_app = WebAppInfo(url = web_app_url)
    )
    keybord = InlineKeyboardMarkup(
        inline_keyboard = [[open_app_button]]        
    )
    id = message.from_user.id
    if  id in admins:
        await message.answer(f"Admin panel")
    else:
        await message.answer(f"Hi message text", reply_markup = keybord)
        if id not in users_id:
            users_id.append(id)

async def periodic_picture_sender():
    for i in range(2):
        await asyncio.sleep(10 * 60)
        
        current_users = list(users_id)
        if not current_users:
            continue
        
        file_path = f'img/tmp/{i+1}.jpg'
        
        photo_to_send = FSInputFile(file_path)
        
        for uid in current_users:
            try:
                await bot.send_photo(
                    chat_id=uid, 
                    photo=photo_to_send,  
                    caption=f"Привет, это мем для тебя из будущего"
                )
            except Exception as e:
                print(f"Ошибка отправки пользователю {uid}: {e}")
            await asyncio.sleep(0.05)