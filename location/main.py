from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    MessageHandler,
    CommandHandler,
    ApplicationBuilder,
    filters
)
from geo_name import get_location_name
import asyncio

TOKEN = "your_bot_token_here"
admin_id = 5050150433


async def start(update, context):
    await update.message.reply_text(
        text="Menu",
        reply_markup=ReplyKeyboardMarkup(
            [[KeyboardButton(text="Location", request_location=True)],
             [KeyboardButton(text="Contact", request_contact=True)]],
            resize_keyboard=True))


async def message(update, context):
    msg = update.message.text
    if msg.lower() == "salom":
        await update.message.reply_text(text="yaxshimisz")


async def contact(update, context):
    msg = update.message.contact.phone_number
    await context.bot.send_message(chat_id=admin_id, text=msg)


async def location(update, context):
    msg = update.message.location
    address = get_location_name(msg.latitude, msg.longitude)
    await context.bot.send_message(chat_id=admin_id, text=address)
    await update.message.reply_text(text=address)


if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, message))
    app.add_handler(MessageHandler(filters.CONTACT, contact))
    app.add_handler(MessageHandler(filters.LOCATION, location))

    asyncio.run(app.run_polling())
