import re
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, ChatAction
from function import send_info, steps, main_menu, send_to_admin


def get_first_name(update, context):
    message = update.message.text
    context.user_data['first_name'] = message
    if context.user_data.get('edit_step'):
        context.user_data['edit_step'] = False
        context.user_data['step'] = steps['main_menu']
        send_info(update, context)
    else:
        context.user_data['step'] = steps['last_name']
        update.message.reply_text(
            text="Enter your last name:",
            reply_markup=ReplyKeyboardRemove()
        )
        update.message.reply_chat_action(action=ChatAction.TYPING)


def get_last_name(update, context):
    message = update.message.text
    context.user_data['last_name'] = message
    if context.user_data.get('edit_step'):
        context.user_data['edit_step'] = False
        context.user_data['step'] = steps['main_menu']
        send_info(update, context)
    else:
        context.user_data['step'] = steps['age']
        update.message.reply_text(
            text="Enter your age:",
            reply_markup=ReplyKeyboardRemove()
        )

def get_age(update, context):
    message = update.message.text
    if re.search('^[0-9]+$', message):
        context.user_data['age'] = message
        if context.user_data.get('edit_step'):
            context.user_data['edit_step'] = False
            context.user_data['step'] = steps['main_menu']
            send_info(update, context)
        else:
            context.user_data['step'] = steps['gender']
            update.message.reply_text(
                text="Choose your gender",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        [
                            KeyboardButton(text="Male"),
                            KeyboardButton(text="Female")
                        ]
                    ],
                    one_time_keyboard=True,
                    resize_keyboard=True
                )
            )
    else:
        update.message.reply_text(
            text="Don't match !!!"
        )


def get_gender(update, context):
    message = update.message.text
    if re.search('^(Male|Female)$', message):
        context.user_data['gender'] = message
        if context.user_data.get('edit_step'):
            context.user_data['edit_step'] = False
            context.user_data['step'] = steps['main_menu']
            send_info(update, context)
        else:
            context.user_data['step'] = steps['contact']
            update.message.reply_text(
                text="Share or send it !",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        [
                            KeyboardButton(text="Share contact", request_contact=True),
                        ]
                    ],
                    one_time_keyboard=True,
                    resize_keyboard=True
                )
            )
    else:
        update.message.reply_text(
            text="Don't match !!!"
        )


def get_text_contact(update, context):
    message = update.message.text
    context.user_data["contact"] = message
    context.user_data['step'] = 6

    if context.user_data.get("edit_step"):
        context.user_data["edit_step"] = False
        send_info(update, context)
    else:
        main_menu(update, context, update.message.from_user.id)
        send_to_admin(update, context)
