from telegram.ext import MessageHandler, ApplicationBuilder, CallbackQueryHandler, filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

ADMIN_ID = 5050150433
TOKEN = "6332933342:AAEMo5e0MEpgYpt8O7hEtWj3Ii9-OSmSlro"
CHANNEL_ID = "-1001864256442"

GLOBAL_LIKE = 0
GLOBAL_DISLIKE = 0


async def Message_handler(update, context):
    context.user_data['choice'] = ""
    buttons = [
        [InlineKeyboardButton(text=f"{GLOBAL_LIKE}  👍", callback_data="like"),
         InlineKeyboardButton(text=f"{GLOBAL_DISLIKE}  👎", callback_data="dislike")]
    ]
    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=update.effective_message.text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


# def Message_handler(update, context):
#     pass


async def inline_handler(update, context):
    query = update.callback_query

    global GLOBAL_LIKE, GLOBAL_DISLIKE

    if query.data == "like":

        if context.user_data.get('choice') == "dislike":
            GLOBAL_DISLIKE -= 1

        if context.user_data.get('choice') != "like":
            GLOBAL_LIKE += 1

        context.user_data["choice"] = "like"

    elif query.data == "dislike":

        if context.user_data.get('choice') == "like":
            GLOBAL_LIKE -= 1

        if context.user_data.get('choice') != "dislike":
            GLOBAL_DISLIKE += 1

        context.user_data["choice"] = "dislike"

    try:
        await context.bot.edit_message_reply_markup(
            chat_id=CHANNEL_ID,
            message_id=query.message.message_id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=f"{GLOBAL_LIKE} 👍", callback_data=f"like"),
                        InlineKeyboardButton(
                            text=f"👎🏿 {GLOBAL_DISLIKE}", callback_data=f"dislike")
                    ]
                ]
            )
        )
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # app.add_handler(CommandHandler('start', start_handler))
    app.add_handler(MessageHandler(Message_handler))
    app.add_handler(CallbackQueryHandler(inline_handler))

    app.run_polling()
