import register
from menu import send_my_info, product


def message_handler(update, context):
    message = update.message.text
    step = context.user_data.get("step", 0)

    if step == 1:
        register.get_first_name(update, context)
    elif step == 2:
        register.get_last_name(update, context)
    elif step == 3:
        register.get_age(update, context)
    elif step == 4:
        register.get_gender(update, context)
    elif step == 5:
        register.get_text_contact(update, context)
    elif step == 6:
        if message == "My Info":
            send_my_info(update, context)
        elif message == "Product":
            product(update, context)
