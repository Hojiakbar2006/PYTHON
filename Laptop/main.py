from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ChatAction

from menu import main_menu, send_my_info
import json

TOKEN = "6332933342:AAE1M1hhnE9BjbU44Drh9FlhYBNmgH-Aj5U"

notebooks = json.loads(open("notebooks.json", "r").read())

def start_handler(update, context):
    user = update.message.from_user
    update.message.reply_chat_action(action=ChatAction.TYPING)
    main_menu(update, context, user.id)


def message_handler(update, context):
    message = update.message.text
    if message == 'Product':
        buttons = []
        for i in range(len(notebooks)):
            buttons.append([InlineKeyboardButton(text=notebooks[i]['title'], callback_data=f"notebooks_element_{i}")])
        buttons.append([InlineKeyboardButton(text="Back", callback_data="notebooks_back")])
        update.message.reply_text(
            text="<b>Choose Notebook:</b>",
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode="HTML"
        )
    elif message == 'My Info':
        send_my_info(update, context)

def inline_handler(update, context):
    query = update.callback_query
    data_sp = str(query.data).split("_")
    if data_sp[0] == 'notebooks':
        if data_sp[1] == 'back':
            context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
            main_menu(update,context, query.message.chat_id)
        elif data_sp[1] == 'element':
            if data_sp[2] == "back":
                context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
                buttons = []
                for i in range(len(notebooks)):
                    buttons.append(
                        [InlineKeyboardButton(text=notebooks[i]['title'], callback_data=f"notebooks_element_{i}")])
                buttons.append([InlineKeyboardButton(text="Back", callback_data="notebooks_back")])
                query.message.reply_text(
                    text="<b>Choose Notebook:</b>",
                    reply_markup=InlineKeyboardMarkup(buttons),
                    parse_mode="HTML"
                )
            else:
                notebook = notebooks[int(data_sp[2])]
                context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
                query.message.reply_photo(
                    photo="https://static.onlinetrade.ru/img/items/b/noutbuk_dell_inspiron_7559_i7_6700hq_16gb_1tb_ssd128gb_gtx_960m_4gb_15.6_touch_uhd_w1064_black_wifi_2.jpg",
                    caption=f"{notebook['title']}\n{notebook['brand']},{notebook['model']}",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Back", callback_data="notebooks_element_back")]])
                )

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
