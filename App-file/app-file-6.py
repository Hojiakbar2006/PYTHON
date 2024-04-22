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
from question import questions


def start_handler(update, context):
    buttons = [
        [InlineKeyboardButton(text=f"{questions[0]['a']}", callback_data="a")],
        [InlineKeyboardButton(text=f"{questions[0]['b']}", callback_data="b")],
        [InlineKeyboardButton(text=f"{questions[0]['c']}", callback_data="c")]
    ]

    context.user_data["question_index"] = 0
    # context.user_data["question_answer"] = []
    context.user_data["question_result"] = 0
    update.message.reply_text(
        text=f"{questions[0]['Savol']}",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    # print(context.user_data["question_answer"])


def inline_handler(update, context):
    query = update.callback_query
    question_index = context.user_data.get("question_index", 0)
    question_count = len(questions)

    if query.data in ["a", "b", "c"]:

        if query.data == questions[question_index]['Javob']:
            context.user_data["question_result"] = context.user_data["question_result"] + 1

        # if context.user_data.get('question_answer'):
        #     answers = context.user_data["question_answer"]
        #     answers.append(query.data)
        # else:
        #     answers = [query.data]
        # context.user_data['question_answer'] = answers

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
            result = 0
            # for i in range(len(questions)):
            #     if questions[i]['Javob'] == context.user_data.get('question_answer')[i]:
            #         result += 1
            query.message.edit_text(
                text=f"Test tugadi! to'g'ri javoblar soni: {question_count}/{context.user_data.get('question_result')}")


TOKEN = "6332933342:AAE1M1hhnE9BjbU44Drh9FlhYBNmgH-Aj5U"

update = Updater(token=TOKEN)
dispatcher = update.dispatcher

dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CallbackQueryHandler(inline_handler))

update.start_polling()
update.idle()

# start_bot: python app-file-6.py
