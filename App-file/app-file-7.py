from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    Filters,
    ConversationHandler
)
from telegram import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

ADMIN_ID = 5050150433
TOKEN = "6332933342:AAE1M1hhnE9BjbU44Drh9FlhYBNmgH-Aj5U"
state = {
    "ism": 1,
    "familya": 2,
    "yosh": 3,
    "jins": 4,
    "telefon": 5,
    "check": 6
}

current_info = {
    "Ism": str,
    "Familya": str,
    "Yosh": int,
    "Jins": str,
    "Telefon": int,
    "Question_result": 0
}
from question import questions


def start(update, context):
    button = [
        [KeyboardButton(text="O'ynash", resize_keyboard=True, one_time_keyboard=True),
         KeyboardButton(text="Ro'yxatdan o'tish", resize_keyboard=True, one_time_keyboard=True)]
    ]
    update.message.reply_text(
        text="Botimizga xush kelibsiz!!!\n",
        reply_markup=ReplyKeyboardMarkup(button)
    )


def separate(update, context):
    message = update.message.text
    if message == "O'ynash":
        buttons = [
            [InlineKeyboardButton(text=f"{questions[0]['a']}", callback_data="a")],
            [InlineKeyboardButton(text=f"{questions[0]['b']}", callback_data="b")],
            [InlineKeyboardButton(text=f"{questions[0]['c']}", callback_data="c")]
        ]

        context.user_data["question_index"] = 0
        update.message.reply_text(
            text=f"{questions[0]['Savol']}",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    if message == "Ro'yxatdan o'tish":
        update.message.reply_text("/signup")


def inline_handler(update, context):
    query = update.callback_query
    question_index = context.user_data.get("question_index", 0)
    question_count = len(questions)

    if query.data in ["a", "b", "c"]:

        if query.data == questions[question_index]['Javob']:
            current_info['Question_result'] += 1

        if question_index < question_count - 1:
            buttons = [
                [InlineKeyboardButton(text=f"{questions[question_index + 1]['a']}", callback_data="a")],
                [InlineKeyboardButton(text=f"{questions[question_index + 1]['b']}", callback_data="b")],
                [InlineKeyboardButton(text=f"{questions[question_index + 1]['c']}", callback_data="c")]
            ]
            query.message.edit_text(
                text=f"{questions[question_index + 1]['Savol']}",
                reply_markup=InlineKeyboardMarkup(buttons)
            )

            context.user_data["question_index"] = question_index + 1
        else:
            context.user_data["question_index"] = 0
            query.message.edit_text(
                text=f"Savol tugadi!!!\n"
                     f"sizning balingiz{len(questions)}/{current_info['Question_result']}"
            )


def sign_up(update, context):
    update.message.reply_text(text="Ismingizni kiriting")
    return state["ism"]


def get_first_name(update, context):
    up_ism = update.message.text
    current_info["Ism"] = up_ism
    update.message.reply_text(text=f"Salom {current_info['Ism']}\nendi familyangizni kiriting:")
    return state["familya"]


def get_last_name(update, context):
    up_familya = update.message.text
    current_info["Familya"] = up_familya
    update.message.reply_text(text=f"{current_info['Ism']} {current_info['Familya']} yoshingizni kiriting:")
    return state["yosh"]


def get_age(update, context):
    up_yosh = update.message.text

    if up_yosh.isnumeric():
        current_info["Yosh"] = up_yosh
        update.message.reply_text(
            text=f"{current_info['Ism']} {current_info['Familya']} jinsingizni tanlang:",
            reply_markup=ReplyKeyboardMarkup([
                [
                    KeyboardButton(text="Erkak"),
                    KeyboardButton(text="Ayol")
                ]
            ])
        )
        return state['jins']
    else:
        update.message.reply_text(text="Yoshingiz raqamlardan iborat bo'lishi kerak:")
        return state['yosh']


def get_gender(update, context):
    up_jins = update.message.text

    if up_jins in ["Erkak", "Ayol"]:
        current_info['Jins'] = up_jins
        update.message.reply_text(
            text="Contactingizni ulashing:",
            reply_markup=ReplyKeyboardMarkup(
                [
                    [KeyboardButton(text='Telefon raqamingizni ulashing',
                                    request_contact=True, resize_keyboard=True,
                                    one_time_keyboard=True)]
                ]
            )
        )
        return state['telefon']
    else:
        update.message.reply_text(text="To'g'ri formatda kiriting:")
        return state['jins']


def get_contact(update, context):
    up_nomer = update.message.contact.phone_number
    current_info['Telefon'] = up_nomer
    update.message.reply_text(
        text=f"Ism: {current_info['Ism']}\n"
             f"Familya: {current_info['Familya']}\n"
             f"Jins: {current_info['Jins']}\n"
             f"Yosh: {current_info['Yosh']}\n"
             f"Telefon: {current_info['Telefon']}",
        reply_markup=InlineKeyboardMarkup(

            [
                [InlineKeyboardButton(text='Saqlash', callback_data="saqlash"),
                 InlineKeyboardButton(text="O'chirish", callback_data="o'chirish")]
            ]

        )
    )
    return state['check']


def check(update, context, ):
    query = update.callback_query
    button = [
        [KeyboardButton(text="O'ynash", resize_keyboard=True, one_time_keyboard=True),
         KeyboardButton(text="Ro'yxatdan o'tish", resize_keyboard=True, one_time_keyboard=True)]
    ]
    if query.data == "saqlash":
        context.user_data[f"{current_info['Ism']}"] = current_info
        query.message.reply_text(text="muvafaqiyatli saqlandi",
                                 reply_markup=ReplyKeyboardMarkup(button)
                                 )


    elif query.data == "o'chirish":
        query.message.edit_text(text="Muvafaqiyatli o'chirildi")
        query.message.reply_text(text="Ismingizni kiriting")
        return state["ism"]


def stop(update, context):
    return ConversationHandler.END


if __name__ == '__main__':
    update = Updater(token=TOKEN)
    dispatcher = update.dispatcher
    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler('signup', sign_up)],
            states={
                1: [MessageHandler(Filters.text, get_first_name)],
                2: [MessageHandler(Filters.text, get_last_name)],
                3: [MessageHandler(Filters.text, get_age)],
                4: [MessageHandler(Filters.text, get_gender)],
                5: [MessageHandler(Filters.contact, get_contact)],
                6: [CallbackQueryHandler(check)],
            },
            fallbacks=[CommandHandler('stop', stop)],
        )
    ),
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))
    dispatcher.add_handler(MessageHandler(Filters.text, separate))

    update.start_polling()
    update.idle()

# start: python app-file-7.py
