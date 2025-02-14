import asyncio
from aiogram import Bot, Dispatcher, F
from app.handlers import router


async def main():
    bot = Bot(token='7656145912:AAFaldWzZmcSw8qPikl0EbsVzj5JEcxCU9c')
    dp = Dispatcher()
    dp.include_router((router))
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(' ')
    except RuntimeError:
        print('Bot is off')