import random
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton


TOKEN = "6586813859:AAEURF7wip4eYTU_9IvKyZXxBLjnwbuBaeE"


def start(update, context):
    # print(random.randint(1, 100))
    context.user_data['words'] = []
    update.message.reply_text(
        text="so'z kirit mazgi", reply_markup=ReplyKeyboardMarkup([[KeyboardButton(text="random so'z")]], resize_keyboard=True))


def message_handler(update, context):
    msg = update.message.text
    print(context.user_data.get('words'))
    if msg == "random so'z":
        num = len(context.user_data.get('words'))-1
        random_number = random.randint(0, num)
        update.message.reply_text(
            text=f"""{context.user_data.get('words')[random_number]}""", reply_markup=ReplyKeyboardMarkup([[KeyboardButton(text="random so'z")]], resize_keyboard=True))
    else:
        context.user_data['words'].append(msg)


if __name__ == "__main__":
    update = Updater(token=TOKEN)
    dispatcher = update.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

    update.start_polling()
    update.idle()
