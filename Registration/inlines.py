from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from menu import main_menu

def inline_handler(update, context):

    query = update.callback_query

    if query.data == "edit_data":
        buttons = [
            [
                InlineKeyboardButton(text="First Name", callback_data="edit_first_name"),
                InlineKeyboardButton(text="Last Name", callback_data="edit_last_name"),
            ],
            [
                InlineKeyboardButton(text="Age", callback_data="edit_age"),
                InlineKeyboardButton(text="Gender", callback_data="edit_gender"),
            ],
            [
                InlineKeyboardButton(text="Contact", callback_data="edit_contact")
            ]
        ]
        query.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif query.data == "edit_first_name":
        query.message.edit_text("Enter First Name!")
        context.user_data['edit_step'] = True
        context.user_data['step'] = 1

    elif query.data == "edit_last_name":
        query.message.edit_text("Enter Last Name!")
        context.user_data['edit_step'] = True
        context.user_data['step'] = 2

    elif query.data == "edit_age":
        query.message.edit_text("Enter Age!")
        context.user_data['edit_step'] = True
        context.user_data['step'] = 3

    elif query.data == "edit_gender":
        buttons = [
            [KeyboardButton(text="Male"), KeyboardButton(text="Female")]
        ]
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text(text="Choose Your Gender!", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True))
        context.user_data['edit_step'] = True
        context.user_data['step'] = 4

    elif query.data == "edit_contact":
        buttons = [
            [KeyboardButton(text="Share", request_contact=True)]
        ]
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text("Share Your Contact Or Send It!", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True))
        context.user_data['edit_step'] = True
        context.user_data['step'] = 5

    elif query.data == "main_menu":
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        main_menu(update, context, query.message.chat_id)
