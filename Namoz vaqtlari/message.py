from function import send_regions


async def handleMessage(update, context):
    msg = update.message.text
    if msg == "Namoz vaqti":
        await send_regions(context, chat_id=update.message.chat_id)
