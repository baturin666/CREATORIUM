import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import openai

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

openai.api_key = OPENAI_API_KEY

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("✍️ Сгенерировать идею"))
    await message.answer("Привет! Я CREATORIUM — AI-креативщик. Нажми кнопку ниже, чтобы получить идею.", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "✍️ Сгенерировать идею")
async def generate_handler(message: types.Message):
    await message.answer("Генерирую идею...")

    prompt = "Придумай идею поста для Instagram на тему бизнеса. Дай заголовок и короткий текст."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7
        )
        text = response.choices[0].message.content
        await message.answer(f"Вот идея:

{text}")
    except Exception as e:
        await message.answer("Произошла ошибка при генерации. Попробуй позже.")
        logging.exception("OpenAI error")

if __name__ == "__main__":
    executor.start_polling(dp)