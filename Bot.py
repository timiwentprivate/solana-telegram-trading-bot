import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Solana Trading Bot\n\n"
        "Welcome! Your bot is online.\n\n"
        "Commands:\n"
        "/status - Check bot status\n"
        "/scan - Token scanner status\n"
        "/balance - Paper trading balance\n"
        "/help - Show commands\n\n"
        "⚠️ Paper trading mode: no real trades."
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Bot status: Online\n"
        "🛡️ Trading mode: Paper trading\n"
        "💰 Real funds: Not connected"
    )


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔎 Token scanner is not connected yet.\n"
        "Next, we will add market data and risk checks."
    )


async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Paper balance: 5,000 virtual units\n"
        "This is simulated money, not your real wallet balance."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start the bot\n"
        "/status - Check status\n"
        "/scan - Scanner status\n"
        "/balance - Simulated balance\n"
        "/help - Show commands"
    )


def main():
    if not BOT_TOKEN:
        raise RuntimeError("Missing TELEGRAM_BOT_TOKEN environment variable")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("scan", scan))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()


if __name__ == "__main__":
    main()
