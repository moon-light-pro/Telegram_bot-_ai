from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import openai

# Set your API keys
TELEGRAM_BOT_TOKEN = "8029274922:AAFyM2w2G4eKh1xEIK0F3FRsLAPg6cF1QP4"
OPENAI_API_KEY = "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"
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
    app.run_polling()

if __name__ == "__main__":
    main()
