import random
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    Filters)
from telegram import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto
)

TOKEN = "6332933342:AAEMo5e0MEpgYpt8O7hEtWj3Ii9-OSmSlro"


def start_handler(update, context):
    global buttons
    buttons = [
        [
            InlineKeyboardButton(text="Send Photo", callback_data="send_photo"),
            InlineKeyboardButton(text="Send Document", callback_data="send_document"),
            InlineKeyboardButton(text="Change Photo", callback_data="change_photo"),
        ],
        [InlineKeyboardButton(text="Send Media Group", callback_data="send_group")]
    ]

    update.message.reply_photo(
        photo='https://picsum.photos/400/300',
        caption="hello",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


def inline_handler(update, context):
    query = update.callback_query
    global buttons
    if query.data == "send_document":
        query.message.reply_document(
            document=open('main.py'),
            caption="birinchi dars",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif query.data == "send_photo":
        query.message.reply_photo(
            photo=f"https://picsum.photos/id/{random.randint(1, 100)}/400/300",
            caption="Random photo",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif query.data == "change_photo":
        query.message.edit_media(
            media=InputMediaPhoto(media=f"https://picsum.photos/id/{random.randint(1, 100)}/400/300"),
        )
        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    elif query.data == "send_group":
        query.message.reply_media_group(
            media=[
                InputMediaPhoto(media=f"https://picsum.photos/id/{random.randint(1, 100)}/400/300"),
                InputMediaPhoto(media=f"https://picsum.photos/id/{random.randint(1, 100)}/400/300"),
                InputMediaPhoto(media=open('photo/photo1.png', 'rb'))
            ]
        )


def photo_handler(update, context):
    file = update.message.photo[-1].file_id
    get_file = context.bot.get_file(file)
    get_file.download("photo/user_photo.png")


def message_handler(update, context):
    if context.user_data.get("matn"):
        words = context.user_data["matn"]
    else:
        words = []
    words.append(update.message.text)
    context.user_data["matn"] = words
    print(f"{update.message.from_user.username}: {words}")

    if len(words) >= 4:
        update.message.reply_text(text="bugunga yatdi borib uclanglar")


update = Updater(token=TOKEN)
dispatcher = update.dispatcher

dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CallbackQueryHandler(inline_handler))
dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

update.start_polling()
update.idle()
