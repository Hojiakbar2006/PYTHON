from telegram.ext import Updater, CommandHandler, MessageHandler,CallbackQueryHandler, Filters
from telegram import ReplyKeyboardMarkup,InlineKeyboardMarkup, KeyboardButton,InlineKeyboardButton, BotCommand
ADMIN_ID = 5050150433
TOKEN = "6332933342:AAE1M1hhnE9BjbU44Drh9FlhYBNmgH-Aj5U"

def start_command(update, context):
    # command_list = [
    #     BotCommand(command="start", description="botni ishga tushirish"),
    #     BotCommand(command="info", description="bot haqida ma'lumot"),
    #     BotCommand(command="menu", description="menular ro'yxati"),
    #     BotCommand(command="settings", description="bot sozlamalari"),
    # ]
    # context.bot.set_my_commands(commands=command_list)
    buttons = [
        [InlineKeyboardButton(text="Dasturlash", callback_data="programming")],
        [InlineKeyboardButton(text="SMM", callback_data="smm")],
    ]
    update.message.reply_text(text=f"<u>Xush kelibsiz</u> <s>{update.message.from_user.first_name}</s> Bo'limni tanlang:",
                              parse_mode='HTML',
                              reply_markup=InlineKeyboardMarkup(buttons))

def inline_messages(update, context):
    query = update.callback_query
    if query.data == "programming":
        buttons = [
            [InlineKeyboardButton(text="backend", callback_data="bd")],
            [InlineKeyboardButton(text="frontend", callback_data="fd")],
        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    if query.data == "bd":
        buttons = [
            [InlineKeyboardButton(text="python", callback_data="py")],
            [InlineKeyboardButton(text="java script", callback_data="js")],
            [InlineKeyboardButton(text="PHP", callback_data="php")]
        ]
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    if query.data == 'py':
        query.message.reply_text(text="Python haqida ma'lumot!!!")
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_command))
dispatcher.add_handler(CallbackQueryHandler(inline_messages))
updater.start_polling()
updater.idle()
