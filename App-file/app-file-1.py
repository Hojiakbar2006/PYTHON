from telegram.ext import Updater, CommandHandler
token = "6332933342:AAE1M1hhnE9BjbU44Drh9FlhYBNmgH-Aj5U"

def start_command(update, context):
    print(update.message.text)
    print(context.bot)
    print(update.message.from_user.id)
    update.message.reply_text(text="Siz /start kamandasini kiritdingiz!")
    context.bot.send_message(chat_id=update.message.from_user.id, text="Ikkinchi xabar!")


updater = Updater(token=token)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_command))

updater.start_polling()
updater.idle()

