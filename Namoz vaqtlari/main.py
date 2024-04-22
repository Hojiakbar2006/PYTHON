from telegram.ext import ApplicationBuilder, filters, CommandHandler, MessageHandler, InlineQueryHandler
from config import TOKEN

from message import handleMessage
from inline import InlineMessageHandler
from function import main_menu


async def start_command(update, context):
    await main_menu(context, update.message.from_user.id)


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))

    app.add_handler(MessageHandler(filters.TEXT, handleMessage))

    app.add_handler(InlineQueryHandler(InlineMessageHandler))

    app.run_polling()


if __name__ == '__main__':
    main()
