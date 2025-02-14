import asyncio
from aiogram import Bot, Dispatcher, F
from app.handlers import router


async def main():
    bot = Bot(token='token')
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
