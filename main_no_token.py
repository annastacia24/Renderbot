
import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
MT5_BRIDGE_URL = os.getenv("MT5_BRIDGE_URL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to RenderBot! Type /trade to place a Smart Money trade.")

async def trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = {
        "symbol": "XAUUSD",
        "action": "buy",
        "lot": 0.1,
        "sl": 100,
        "tp": 200
    }
    try:
        response = requests.post(f"{MT5_BRIDGE_URL}/trade", json=data)
        await update.message.reply_text(f"Trade sent: {response.json()}")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("trade", trade))
    app.run_polling()
