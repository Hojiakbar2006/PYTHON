import function
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    Filters
)
from message_handler import message_handler, contact_handler
from inline_message_handler import inline_message_handler
TOKEN = "6332933342:AAE1M1hhnE9BjbU44Drh9FlhYBNmgH-Aj5U"


if __name__ == '__main__':
    update = Updater(token=TOKEN)
    dispatcher = update.dispatcher

    dispatcher.add_handler(CommandHandler('start', function.start_handler))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(CallbackQueryHandler(inline_message_handler))

    update.start_polling()
    update.idle()