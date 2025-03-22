from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import openai
import os

# Load API keys from environment variables
TELEGRAM_BOT_TOKEN = os.getenv("8029274922:AAFyM2w2G4eKh1xEIK0F3FRsLAPg6cF1QP4")
OPENAI_API_KEY = os.getenv("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")

openai.api_key = OPENAI_API_KEY

async def start(update: Update, context):
    await update.message.reply_text("Hello! I'm an AI bot. Ask me anything!")

async def chat(update: Update, context):
    user_message = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    reply_text = response["choices"][0]["message"]["content"]
    await update.message.reply_text(reply_text)

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
