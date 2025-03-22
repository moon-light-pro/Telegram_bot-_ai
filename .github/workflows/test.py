from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = "8029274922:AAFyM2w2G4eKh1xEIK0F3FRsLAPg6cF1QP4"

async def start(update: Update, context):
    await update.message.reply_text("Test successful! Bot is working.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
