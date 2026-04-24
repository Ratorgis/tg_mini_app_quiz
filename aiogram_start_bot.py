import asyncio
from presentation.create_bot import dp, bot
from utils.handlers.commands import user_router, periodic_picture_sender

async def main():
    dp.include_router(user_router)
    await bot.delete_webhook(drop_pending_updates=True)    
    asyncio.create_task(periodic_picture_sender())
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    