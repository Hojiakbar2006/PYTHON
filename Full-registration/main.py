from telegram import BotCommand, ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from telegram.ext import Updater, Filters, CallbackQueryHandler, MessageHandler, CommandHandler

from config import steps, token
from function import main_menu
from message_handler import message_handler

# from database import BaseCRUD
# users = BaseCRUD("users.db", "users")


def start(update, context):
	context.user_data['edit_step'] = False
	chat_id = update.message.from_user.id
	# print(users.get_all())
	if chat_id != context.user_data.get('chat_id', 0):
		context.user_data['step'] = steps["first_name"]
		update.message.reply_text(text="Enter your first name")
	else:
		main_menu(update, context)


if __name__ == "__main__":
	updater = Updater(token)
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start', start))
	dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
	dispatcher.add_handler(MessageHandler(Filters.contact, start))
	dispatcher.add_handler(MessageHandler(Filters.location, start))
	dispatcher.add_handler(CallbackQueryHandler(start))

	updater.start_polling()
	updater.idle()
