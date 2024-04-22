from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler
from database import Database

ADMIN_ID = 5050150433
TOKEN = "6332933342:AAEMo5e0MEpgYpt8O7hEtWj3Ii9-OSmSlro"

db = Database("user_db")


def start_handler(update, context):
    pass
    # check(update, context)


def inline_handler(update, context):
    query = update.callback_query
    data_sp = str(query.data).split("_")

def contact_handler(update, context):
    message = update.message.contact.phone_number
    user = update.message.from_user


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))

    updater.start_polling()
    updater.idle()

