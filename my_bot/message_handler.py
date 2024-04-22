import register
from function import send_info, main_menu, show_product_buttons
from telegram import ReplyKeyboardRemove


###star_message

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
            send_info(update, context)
        elif message == "Product":
            update.message.reply_text(
                text="Our product 👇",
                reply_markup=ReplyKeyboardRemove()
            )
            show_product_buttons(update, context)


def contact_handler(update, context):
    step = context.user_data.get('step', 0)
    user = update.message.from_user
    if step == 5:
        context.user_data["contact"] = update.message.contact.phone_number
        context.user_data['step'] = 6
        main_menu(update, context, user.id)
