from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler
from telegram import ReplyKeyboardRemove
from database import *
from commons import *

TOKEN = "6332933342:AAE1M1hhnE9BjbU44Drh9FlhYBNmgH-Aj5U"


db = Database("sample-database.db")

def start_handler(update, context):
    main_menu(
        context=context,
        chat_id=update.message.from_user.id
    )


def message_handler(update, context):
    message = update.message.text
    if message == "Regions":
        regions = db.get_all_regions()
        send_regions(
            context=context,
            regions=regions,
            chat_id=update.message.from_user.id
        )


def inline_handler(update, context):
    query = update.callback_query
    data_sp = str(query.data).split("_")
    if data_sp[0] == "region":
        if data_sp[1] == "back":
            regions = db.get_all_regions()
            send_regions(
                context=context,
                regions=regions,
                chat_id=query.message.chat_id,
                message_id=query.message.message_id
            )
        elif data_sp[1] == "country":
            countries = db.get_countries_by_region(int(data_sp[2]))
            send_countries(
                context=context,
                countries=countries,
                chat_id=query.message.chat_id,
                message_id=query.message.message_id
            )
        else:
            countries = db.get_countries_by_region(int(data_sp[1]))
            send_countries(
                context=context,
                countries=countries,
                chat_id=query.message.chat_id,
                message_id=query.message.message_id
            )
    if query.data == "close":
        main_menu(context=context, chat_id=query.message.chat_id)


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))

    updater.start_polling()
    updater.idle()
