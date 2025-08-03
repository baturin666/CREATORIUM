import logging
import os
import openai
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

# Настройки логирования
logging.basicConfig(level=logging.INFO)

# Токены и ключи
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Инициализация бота и OpenAI
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
openai.api_key = OPENAI_API_KEY

# Обработка команды /start
@dp.message_handler(commands=["start"])
async def start_handler(message: Message):
    await message.answer("Привет! Я AI-бот. Напиши мне что-нибудь, и я отвечу.")

# Обработка всех остальных сообщений
@dp.message_handler()
async def handle_message(message: Message):
    try:
        user_input = message.text

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        reply = response.choices[0].message["content"]
        await message.answer(reply)

    except Exception as e:
        await message.answer("Произошла ошибка. Попробуй позже.")
        logging.exception(e)

# Запуск
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
