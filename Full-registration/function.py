from telegram import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup

from config import steps
from database import BaseCRUD
users = BaseCRUD("users.db", "users")

def get_first_name(update, context):
	message = update.message.text
	chat_id = update.message.from_user.id
	context.user_data['first_name'] = message
	if context.user_data['edit_step']:
		users.update(chat_id, first_name=message)
		context.user_data['edit_step'] = False
	else:
		context.user_data['step'] = steps["last_name"]
		update.message.reply_text(
			text="Enter your last Name:",
			reply_markup=ReplyKeyboardRemove()
		)


def get_last_name(update, context):
	message = update.message.text
	chat_id = update.message.from_user.id
	context.user_data['last_name'] = message
	if context.user_data['edit_step']:
		users.update(chat_id, last_name=message)
		context.user_data['edit_step'] = False
	else:
		context.user_data['step'] = steps["age"]
		update.message.reply_text(
			text="Enter your age:",
			reply_markup=ReplyKeyboardRemove()
		)


def get_age(update, context):
	message = int(update.message.text)
	chat_id = update.message.from_user.id
	context.user_data['age'] = message
	if context.user_data['edit_step']:
		users.update(chat_id, age=message)
		context.user_data['edit_step'] = False
	else:
		context.user_data['step'] = steps["gender"]
		update.message.reply_text(
			text='Enter your gender "Male/Famale"',
			reply_markup=ReplyKeyboardMarkup(
				[
					[KeyboardButton(text="Male", ),
					 KeyboardButton(text="Famale")]
				],
				one_time_keyboard=True,
				resize_keyboard=True
			)
		)


def get_gender(update, context):
	message = update.message.text
	chat_id = update.message.from_user.id
	context.user_data['gender'] = message
	if context.user_data['edit_step']:
		users.update(chat_id, gender=message)
		context.user_data['edit_step'] = False
	else:
		context.user_data['step'] = steps["phone_number"]
		update.message.reply_text(
			text="Enter your phone number ex:+998#########",
			reply_markup=ReplyKeyboardRemove()
		)


def get_phone_number(update, context):
	message = update.message.text
	chat_id = update.message.from_user.id
	context.user_data['phone_number'] = message
	if context.user_data['edit_step']:
		users.update(chat_id, phone_number=message)
		context.user_data['edit_step'] = False
	else:
		context.user_data['step'] = steps["location"]
		update.message.reply_text(
			text='Enter your address "city/region"',
			reply_markup=ReplyKeyboardRemove()
		)


def get_address(update, context):
	message = update.message.text
	chat_id = update.message.from_user.id
	context.user_data['location'] = message
	if context.user_data['edit_step']:
		users.update(chat_id, phone_number=message)
		context.user_data['edit_step'] = False
	else:
		context.user_data['step'] = 0
		reply_markup = ReplyKeyboardMarkup(
			[
				[
					KeyboardButton(text="Edit"),
					KeyboardButton(text="Save"),
				]
			],
			one_time_keyboard=True,
			resize_keyboard=True
		)
		update.message.reply_text(text="Do you want to save the information?", reply_markup=reply_markup)


def send_to_db(update, context):
	chat_id = update.message.from_user.id
	user_name = update.message.from_user.username
	data = context.user_data
	users.insert(
		first_name=data["first_name"],
		last_name=data["last_name"],
		age=data["age"],
		gender=data["gender"],
		phone_number=data["phone_number"],
		location=data["location"],
		latitude=data.get("latitude", None),
		longitude=data.get("longitude", None),
		chat_id=chat_id,
		user_name=user_name,
	)

	context.user_data['chat_id'] = chat_id
	update.message.reply_text(text="Saved to base", reply_markup=ReplyKeyboardRemove())
	context.user_data['step'] = steps["main_menu"]
	print(users.get_all())


def main_menu(update, context):
	reply_markup = ReplyKeyboardMarkup(
		[
			[KeyboardButton(text="Main menu"),
			 KeyboardButton(text="My info")]
		],
		one_time_keyboard=True,
		resize_keyboard=True
	)
	update.message.reply_text(text="Main menu", reply_markup=reply_markup)
