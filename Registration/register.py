import re
from telegram import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from menu import main_menu, send_my_info

def get_first_name(update, context):
    message = update.message.text
    context.user_data['first_name'] = message
    if context.user_data.get("edit_step"):
        context.user_data['edit_step'] = False
        context.user_data['step'] = 6
    else:
        context.user_data['step'] = 2
        update.message.reply_text(
            text="Enter Last Name:",
            reply_markup=ReplyKeyboardRemove()
        )
def get_last_name(update, context):
    message = update.message.text
    context.user_data['last_name'] = message
    if context.user_data.get("edit_step"):
        context.user_data["edit_step"] = False
        context.user_data["step"] = 6
        send_my_info(update, context)

    else:
        context.user_data['step'] = 3
        update.message.reply_text(
            text=f"Enter Your Age!",
            reply_markup=ReplyKeyboardRemove()
        )

def get_last_name(update, context):
    message = update.message.text
    context.user_data['last_name'] = message
    if context.user_data.get("edit_step"):
        context.user_data["edit_step"] = False
        context.user_data["step"] = 6
        send_my_info(update, context)

    else:
        context.user_data['step'] = 3
        update.message.reply_text(
            text=f"Enter Your Age!",
            reply_markup=ReplyKeyboardRemove()
        )


def get_age(update, context):
    message = update.message.text
    if re.search('^[0-9]+$', message):
        context.user_data['age'] = message
        if context.user_data.get("edit_step"):
            context.user_data["edit_step"] = False
            context.user_data["step"] = 6
            send_my_info(update, context)

        else:
            context.user_data['step'] = 4
            buttons = [
                [KeyboardButton(text="Male"), KeyboardButton(text="Female")]
            ]
            update.message.reply_text(
                text=f"Choose Your Gender!",
                reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
            )
    else:
        update.message.reply_text(
            text=f"Please Enter True Value!!!",
        )


def get_gender(update, context):
    message = update.message.text
    if re.search('^(Male|Female)$', message):
        context.user_data['gender'] = message
        if context.user_data.get("edit_step"):
            context.user_data["edit_step"] = False
            context.user_data["step"] = 6
            send_my_info(update, context)

        else:
            context.user_data['step'] = 5
            buttons = [
                [KeyboardButton(text="Share", request_contact=True)]
            ]
            update.message.reply_text(
                text=f"Share Your Contact Or Send It",
                reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
            )
    else:
        update.message.reply_text(
            text=f"Please Enter True Value!!!",
        )


def get_text_contact(update, context):
    message = update.message.text
    context.user_data["contact"] = message
    context.user_data['step'] = 6

    if context.user_data.get("edit_step"):
        context.user_data["edit_step"] = False
        send_my_info(update, context)
    else:
        main_menu(update, context, message.from_user.id)
