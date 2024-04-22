from telegram import ReplyKeyboardMarkup, KeyboardButton

from function import (get_first_name,
                      get_last_name,
                      get_age,
                      get_gender,
                      get_phone_number,
                      get_address,
                      main_menu, send_to_db, )


def message_handler(update, context):
	message = update.message.text
	step = context.user_data.get("step", 0)

	if step == 1:
		get_first_name(update, context)
	elif step == 2:
		get_last_name(update, context)
	elif step == 3:
		get_age(update, context)
	elif step == 4:
		get_gender(update, context)
	elif step == 5:
		get_phone_number(update, context)
	elif step == 6:
		get_address(update, context)
	elif message == "Save":
		send_to_db(update, context)
	elif step == 8:
		main_menu(update, context)


# if message == "My Info":
# 	send_my_info(update, context)
# elif message == "Product":
# 	product(update, context)
