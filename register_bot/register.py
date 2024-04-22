import logging
import sqlite3

from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters

from geo_name import get_location_name

token = "6913784384:AAHvK3DaTTWBKcS7DXZxS3brH02zdoTWItU"
admin_id = 5050150433

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users
    (phone_number TEXT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    gender TEXT,
    address TEXT,
    latitude REAL,
    longitude REAL);
""")

connect.commit()


def start(update, context):
	reply_text = "Salom telefon raqamingizni ulashing"
	reply_markup = ReplyKeyboardMarkup([
		[KeyboardButton(text="Telefon raqamizni ulashing", request_contact=True)]
	], resize_keyboard=True, one_time_keyboard=True)
	context.bot.send_message(chat_id=update.effective_user.id, text=reply_text, reply_markup=reply_markup)
	logging.info(f"user - {update.effective_user.id} started ")
	return 'PHONE_NUMBER'


def phone_number(update, context):
	phone_number = update.message.contact.phone_number
	context.user_data['phone_number'] = phone_number
	update.message.reply_text(text="Ismingizni kiriting")
	return 'FIRST_NAME'


def first_name(update, context):
	first_name = update.message.text
	context.user_data['first_name'] = first_name
	update.message.reply_text(text="Familyangizni kiriting")
	return 'LAST_NAME'


def last_name(update, context):
	last_name = update.message.text
	context.user_data['last_name'] = last_name
	update.message.reply_text(text="Yoshingizni kiriting")
	return 'AGE'


def age(update, context):
	age = update.message.text
	context.user_data['age'] = age
	update.message.reply_text(text="Jinsingizni kiriting ('erkak/ayol')")
	return 'GENDER'


def gender(update, context):
	gender = update.message.text
	context.user_data['gender'] = gender
	reply_text = "Lokatsiyangizni ulashing"
	reply_markup = ReplyKeyboardMarkup([
		[KeyboardButton(text="Lokatsiyangizni ulashing", request_location=True)]
	], resize_keyboard=True, one_time_keyboard=True)
	update.message.reply_text(text=reply_text, reply_markup=reply_markup)
	return 'GEOLOCATION'


def location(update, context):
	latitude = update.message.location.latitude
	longitude = update.message.location.longitude
	address = get_location_name(latitude, longitude)
	context.user_data['latitude'] = latitude
	context.user_data['longitude'] = longitude
	context.user_data['location'] = address
	conn = sqlite3.connect("users.db")
	c = conn.cursor()
	c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (
		context.user_data['phone_number'],
		context.user_data['first_name'],
		context.user_data['last_name'],
		context.user_data['age'],
		context.user_data['gender'],
		context.user_data['location'],
		context.user_data['latitude'],
		context.user_data['longitude'],
	))
	conn.commit()
	conn.close()
	logging.info("User registered")
	update.message.reply_text(text="Rahmat")
	update.message.reply_text(text=f"""
		Ismingiz:{context.user_data['first_name'],}
		Familyangiz:{context.user_data['last_name'],}
		Yoshingiz:{context.user_data['age'],}
		phone:{context.user_data['phone_number'],}
		manzilingiz:{context.user_data['location'],}
		latitude:{context.user_data['latitude'],}
		longitude:{context.user_data['longitude'],}
	""", reply_markup=ReplyKeyboardRemove())
	context.bot.send_message(chat_id=admin_id, text=f"""
		Ismingiz:{context.user_data['first_name'],}
		Familyangiz:{context.user_data['last_name'],}
		Yoshingiz:{context.user_data['age'],}
		phone:{context.user_data['phone_number'],}
		manzilingiz:{context.user_data['location'],}
		latitude:{context.user_data['latitude'],}
		longitude:{context.user_data['longitude'],}
	""")
	return ConversationHandler.END


def cancel(update, context):
	update.message.reply_text(text="bekor qilindi")
	return ConversationHandler.END


if __name__ == "__main__":
	updater = Updater(token)
	dispatcher = updater.dispatcher

	cov_handler = ConversationHandler(
		entry_points=[CommandHandler('start', start)],
		states={
			'PHONE_NUMBER': [MessageHandler(Filters.contact & ~Filters.command, phone_number)],
			'FIRST_NAME': [MessageHandler(Filters.text & ~Filters.command, first_name)],
			'LAST_NAME': [MessageHandler(Filters.text & ~Filters.command, last_name)],
			'AGE': [MessageHandler(Filters.text & ~Filters.command, age)],
			'GENDER': [MessageHandler(Filters.text & ~Filters.command, gender)],
			'GEOLOCATION': [MessageHandler(Filters.location & ~Filters.command, location)],
		},
		fallbacks=[CommandHandler("cancel", cancel)]
	)
	dispatcher.add_handler(cov_handler)

	updater.start_polling()
	updater.idle()
