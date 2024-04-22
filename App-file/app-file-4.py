# start: python dastur.py

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand

ADMIN_ID = 5050150433
TOKEN = "6332933342:AAE1M1hhnE9BjbU44Drh9FlhYBNmgH-Aj5U"


def start(update, context):
    command_list = [
        BotCommand(command="start", description="botni faollashtirish"),
    ]
    context.bot.set_my_commands(commands=command_list)

    buttons = [
        [InlineKeyboardButton(text="Dasturlash", callback_data="programming")],
        [InlineKeyboardButton(text="SMM", callback_data="smm")],
    ]
    update.message.reply_text(
        text="Tanlang",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


def inline_hand(update, context):
    query = update.callback_query
    if query.data == "programming":
        buttons = [
            [InlineKeyboardButton(text="backend", callback_data="bd")],
            [InlineKeyboardButton(text="frontend", callback_data="fd")],
        ]
        query.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons))
    if query.data == "bd":
        buttons = [
            [InlineKeyboardButton(text="python", callback_data="py")],
            [InlineKeyboardButton(text="java script", callback_data="js")],
            [InlineKeyboardButton(text="PHP", callback_data="php")]
        ]
        query.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons))
    if query.data == 'py':
        query.message.reply_text(text="Python haqida ma'lumot!!!")


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(inline_hand))

    updater.start_polling()
    updater.idle()


main()
