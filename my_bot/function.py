import json
from telegram import (
    ChatAction,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
)

notebooks = json.loads(open("notebooks.json", "r").read())
steps = {
    "first_name": 1,
    "last_name": 2,
    "age": 3,
    "gender": 4,
    "contact": 5,
    "main_menu": 6,
}


#####start
def start_handler(update, context):
    user = update.message.from_user
    update.message.reply_chat_action(action=ChatAction.TYPING)
    if context.user_data.get('first_name'):
        main_menu(update, context, user.id)
    else:
        context.user_data['step'] = steps["first_name"]
        update.message.reply_text(
            text='Enter yor firstname',
            reply_markup=ReplyKeyboardRemove()
        )


def send_info(update, context):
    data = context.user_data
    buttons = [
        [
            InlineKeyboardButton(text="Edit Data", callback_data="edit_data"),
        ],
        [
            InlineKeyboardButton(text="Main Menu", callback_data="main_menu"),
        ]
    ]
    msg = update.message.reply_text(
        text="🕓",
        reply_markup=ReplyKeyboardRemove(),
    )
    context.bot.delete_message(chat_id=update.message.chat_id, message_id=msg.message_id)
    update.message.reply_text(
        text=f"<b>First Name</b>: {data['first_name']}\n"
             f"<b>Last Name</b>:{data['last_name']}\n"
             f"<b>Age</b>: {data['age']}\n"
             f"<b>Gender</b>: {data['gender']}\n"
             f"<b>Phone Number</b>: {data['contact']}",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode="HTML"
    )

def send_to_admin(update, context):
    data = context.user_data
    if context.user_data.get("first_name"):
        context.bot.edit_message(
            chat_id=5050150433,
            text=f"<b>First Name</b>: {data['first_name']}\n"
                 f"<b>Last Name</b>:{data['last_name']}\n"
                 f"<b>Age</b>: {data['age']}\n"
                 f"<b>Gender</b>: {data['gender']}\n"
                 f"<b>Phone Number</b>: {data['contact']}",
            parse_mode="HTML"
        )


def main_menu(update, context, chat_id):
    buttons = [
        [
            KeyboardButton(text="Product"), KeyboardButton(text="My Info"),
        ]
    ]
    context.bot.send_message(
        chat_id=chat_id,
        text="Main Menu",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )


def show_product_buttons(update, context):
    buttons = []
    for i in range(len(notebooks)):
        buttons.append([InlineKeyboardButton(text=f"{notebooks[i]['title']},", callback_data=f"notebook_element_{i}")])
    buttons.append([InlineKeyboardButton(text="Back", callback_data=f"notebook_back")])
    update.message.reply_text(
        text="Please Choose One !!!",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
