import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("8924319394:AAFZSOqXSOu_tSV8znrQVh2U7UpXaiCuyms")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я AI-ассистент группы."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Бот запущен!")

app.run_polling()