# CREATORIUM AI (Telegram бот с генерацией через OpenAI)

## 🚀 Быстрый запуск на Render

1. Перейди на https://render.com и создай новый Web Service
2. Нажми "Deploy from GitHub" или "Deploy from ZIP" (если вручную)
3. Укажи:
   - Build Command: pip install -r requirements.txt
   - Start Command: python main.py
4. Перейди в Settings → Environment
5. Добавь переменные окружения:
   - BOT_TOKEN = (токен твоего Telegram-бота от BotFather)
   - OPENAI_API_KEY = (ключ OpenAI)

6. Нажми "Deploy" — и бот заработает

📌 Бот отвечает на /start и кнопку "✍️ Сгенерировать идею"
📌 Используется модель gpt-3.5-turbo