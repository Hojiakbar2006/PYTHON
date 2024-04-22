from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
from database import Data

data = Data("data.db")


async def main_menu(context, chat_id):
    buttons = [
        [
            KeyboardButton(text="Namoz vaqti"),
            KeyboardButton(text="Ma'lumot")
        ]
    ]
    await context.bot.send_message(
        chat_id=chat_id,
        text="Asosiy oyna",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )


def remove_inline(query, context, message_id):
    query.message.edit_text(
        text="🕓",
        reply_markup=None,
    )
    context.bot.delete_message(
        chat_id=query.message.chat_id, message_id=message_id)


async def send_regions(context, chat_id, message_id=None):
    regions = data.get_regions()
    buttons = [[InlineKeyboardButton(text=regions[0]['region_name'], callback_data=f"region_{regions[0]['id']}"),
                InlineKeyboardButton(text=regions[1]['region_name'], callback_data=f"region_{regions[1]['id']}")],
               [InlineKeyboardButton(text=regions[2]['region_name'], callback_data=f"region_{regions[2]['id']}"),
                InlineKeyboardButton(text=regions[3]['region_name'], callback_data=f"region_{regions[3]['id']}")],
               [InlineKeyboardButton(text=regions[4]['region_name'], callback_data=f"region_{regions[4]['id']}"),
                InlineKeyboardButton(text=regions[5]['region_name'], callback_data=f"region_{regions[5]['id']}")],
               [InlineKeyboardButton(text=regions[6]['region_name'], callback_data=f"region_{regions[6]['id']}"),
                InlineKeyboardButton(text=regions[7]['region_name'], callback_data=f"region_{regions[7]['id']}")],
               [InlineKeyboardButton(text=regions[8]['region_name'], callback_data=f"region_{regions[8]['id']}"),
                InlineKeyboardButton(text=regions[9]['region_name'], callback_data=f"region_{regions[9]['id']}")],
               [InlineKeyboardButton(text=regions[10]['region_name'], callback_data=f"region_{regions[10]['id']}"),
                InlineKeyboardButton(text=regions[11]['region_name'], callback_data=f"region_{regions[11]['id']}")],
               [InlineKeyboardButton(text=regions[12]['region_name'], callback_data=f"region_{
                                     regions[12]['id']}")],
               [InlineKeyboardButton(text="Asosiy oyna", callback_data="main_menu")]]
    if message_id:
        await context.bot.edit_message_text(
            chat_id=chat_id,
            text="Viloyatlardan birini tanlang",
            reply_markup=InlineKeyboardMarkup(buttons),
            message_id=message_id
        )
    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Viloyatlardan birini tanlang",
            reply_markup=InlineKeyboardMarkup(buttons)
        )


async def send_cities(context, chat_id, data_sp, message_id=None):
    buttons = []
    cities = data.get_cities()

    for i in cities:
        buttons.append([InlineKeyboardButton(
            text=i['city_name'], callback_data=f"city_{i['path']}")])
    buttons.append([InlineKeyboardButton(
        text="Back", callback_data="region_back")])

    if message_id:
        await context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Viloyat tanlang",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Shahar tanlang",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
