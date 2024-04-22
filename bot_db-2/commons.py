from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def main_menu(context, chat_id, message_id=None):
    buttons = [
        [
            KeyboardButton(text="Regions"),
            KeyboardButton(text="Jobs")
        ]
    ]
    context.bot.send_message(
        chat_id=chat_id,
        text="Menu",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )


def send_regions(context, regions, chat_id, message_id=None):
    buttons = []
    for region in regions:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=f"{region['region_name']}",
                    callback_data=f"region_{region['region_id']}")
            ]
        )
    buttons.append([InlineKeyboardButton(text="Close", callback_data="close")])

    if message_id:
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="<b>Choose regions</b>",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=buttons
            ),
            parse_mode="HTML"
        )
    else:
        context.bot.send_message(
            chat_id=chat_id,
            text="<b>Choose regions</b>",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=buttons
            ),
            parse_mode="HTML"
        )

def send_countries(context, countries, chat_id, message_id=None):
    buttons = []
    for country in countries:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=f"{country['country_name']}",
                    callback_data=f"region_country{country['region_id']}"
                )
            ]
        )
    buttons.append([InlineKeyboardButton(text="back", callback_data="region_back")])

    if message_id:
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="<b>Choose countries</b>",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=buttons
            ),
            parse_mode="HTML"
        )
    else:
        context.bot.send_message(
            chat_id=chat_id,
            text="<b>Choose countries</b>",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=buttons
            ),
            parse_mode="HTML"
        )


