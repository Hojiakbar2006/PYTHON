from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton

ADMIN_ID = 5050150433
TOKEN = "6332933342:AAE1M1hhnE9BjbU44Drh9FlhYBNmgH-Aj5U"


def start_command(update, context):
    update.message.reply_text(text="Siz /start kamandasini kiritdingiz!")
    context.bot.send_message(chat_id=ADMIN_ID, text="bot faol holatda")


def show_menu(update, context):
    buttons = [
        [KeyboardButton(text="Send Contact", request_contact=True)],
        [KeyboardButton(text="Send Location", request_location=True)]
    ]
    update.message.reply_text(
        text="Menu",
        reply_markup=ReplyKeyboardMarkup(
            buttons, resize_keyboard=True, one_time_keyboard=True)
    )


def message_handler(update, context):
    message = update.message.text
    update.message.reply_text(f"sizning xabaringiz {message}")


def contact_handler(update, context):
    phone_number = update.message.contact.phone_number
    context.bot.send_message(
        chat_id=ADMIN_ID, text=f"yangi foydalanuvchi {phone_number}")


def location_handler(update, context):
    location = update.message.location
    context.bot.send_message(
        chat_id=ADMIN_ID, latitude=location.latitude, longtidude=location.longtidude)


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('menu', show_menu))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(MessageHandler(Filters.location, location_handler))

    updater.start_polling()
    updater.idle()


main()
