import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# ВСТАВЬ СВОЙ НОВЫЙ ТОКЕН ВНУТРЬ КАВЫЧЕК
TOKEN = '8815423174:AAHUIAsgZyURtSPg6i-_e5NQcR1OHipHVj4'

# Пока здесь будет тестовая ссылка
WEBAPP_URL = 'https://google.com' 

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎴 Открыть Альбом Карточек", web_app=WebAppInfo(url=WEBAPP_URL))]
    ])
    
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n"
        "Добро пожаловать в игру по сбору хоккейных карточек КХЛ!\n"
        "Жми на кнопку ниже, чтобы начать.", 
        reply_markup=kb
    )

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
