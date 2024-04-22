###start_inline
from telegram import ChatAction, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from function import steps, main_menu, show_product_buttons, notebooks


def inline_message_handler(update, context):
    query = update.callback_query
    product_query = str(query.data).split("_")
    if query.data == "edit_data":
        buttons = [
            [
                InlineKeyboardButton(text="First name", callback_data="first_name"),
                InlineKeyboardButton(text="Last name", callback_data="last_name")
            ],
            [
                InlineKeyboardButton(text="Age", callback_data="age"),
                InlineKeyboardButton(text="Gender", callback_data="gender")
            ],
            [
                InlineKeyboardButton(text="Contact", callback_data="contact")
            ],
        ]
        query.message.edit_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif query.data == "main_menu":
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        main_menu(update, context, query.message.chat_id)
    elif query.data == "first_name":
        context.user_data["step"] = steps["first_name"]
        context.user_data["edit_step"] = True
        query.message.edit_text(
            "Enter your firstname"
        )
    elif query.data == "last_name":
        context.user_data["step"] = steps["last_name"]
        context.user_data["edit_step"] = True
        query.message.edit_text(
            "Enter your lastname"
        )
    elif query.data == "age":
        context.user_data["step"] = steps["age"]
        context.user_data["edit_step"] = True
        query.message.edit_text(
            "Enter your age"
        )
    elif query.data == "gender":
        buttons = [
            [KeyboardButton(text="Male"), KeyboardButton(text="Female")]
        ]
        context.bot.delete_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id
        )
        query.message.reply_text(
            text="Choose Your Gender!",
            reply_markup=ReplyKeyboardMarkup(
                buttons,
                resize_keyboard=True,
                one_time_keyboard=True))
        context.user_data['edit_step'] = True
        context.user_data['step'] = steps["gender"]

    elif query.data == "contact":
        buttons = [
            [
                KeyboardButton(
                    text="Share",
                    request_contact=True
                )
            ]
        ]
        context.bot.delete_message(
            chat_id=query.message.chat_id,
            message_id=query.message.message_id
        )
        query.message.reply_text(
            text="Share Your Contact Or Send It!",
            reply_markup=ReplyKeyboardMarkup(
                buttons,
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )
        context.user_data['edit_step'] = True
        context.user_data['step'] = steps["contact"]
    elif product_query[0] == "notebook":
        if product_query[1] == "element":
            notebook = notebooks[int(product_query[-1])]
            context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
            query.message.reply_photo(
                photo="https://static.onlinetrade.ru/img/items/b"
                      "/noutbuk_dell_inspiron_7559_i7_6700hq_16gb_1tb_ssd128gb_gtx_960m_4gb_15"
                      ".6_touch_uhd_w1064_black_wifi_2.jpg",
                caption=f"{notebook['title']}\n{notebook['brand']},{notebook['model']}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Back",
                                callback_data="notebook_back"
                            )
                        ]
                    ]
                )
            )
        elif product_query[-1] == "back":
            if product_query[-1] == "back":
                context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
                main_menu(update, context, query.message.chat_id)
