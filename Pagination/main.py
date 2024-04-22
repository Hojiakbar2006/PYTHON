from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler

TOKEN = ""
# Constants for pagination
items_per_page = 5  # Number of items per page
current_page = 1  # Current page

# Example data for pagination
data_from_db = [
    "Item 1",
    "Item 2",
    "Item 3",
    "Item 4",
    "Item 5",
    "Item 6",
    "Item 7",
    "Item 8",
    "Item 9",
    "Item 10",
    "Item 11",
    "Item 12",
]

# Function to handle the /start command


def start(update, context):
    # Get the chat ID
    chat_id = update.effective_chat.id

    # Generate the inline keyboard for the current page
    reply_markup = generate_inline_keyboard()

    # Send the message with the inline keyboard
    context.bot.send_message(
        chat_id=chat_id, text="Select an item:", reply_markup=reply_markup)

# Function to generate the inline keyboard for the current page


def generate_inline_keyboard():
    # Calculate start and end indices based on the current page
    start_index = (current_page - 1) * items_per_page
    end_index = start_index + items_per_page

    # Get the items for the current page
    items = data_from_db[start_index:end_index]

    # Generate the inline keyboard buttons for the items
    keyboard_buttons = [
        [InlineKeyboardButton(item, callback_data=item)] for item in items
    ]

    # Add previous and next buttons for pagination
    pagination_buttons = []
    if current_page > 1:
        pagination_buttons.append(InlineKeyboardButton(
            "<< orqaga", callback_data="previous"))
    if end_index < len(data_from_db):
        pagination_buttons.append(InlineKeyboardButton(
            "oldinga >>", callback_data="next"))

    # Add the pagination buttons to the keyboard
    if pagination_buttons:
        keyboard_buttons.append(pagination_buttons)

    # Create the inline keyboard markup
    reply_markup = InlineKeyboardMarkup(keyboard_buttons)

    return reply_markup

# Function to handle button presses


def button_press(update, context):
    query = update.callback_query
    query.answer()

    # Handle the callback based on the pressed button
    button_data = query.data

    if button_data == "previous":
        previous_page()
    elif button_data == "next":
        next_page()

    # Edit the message with the updated inline keyboard
    reply_markup = generate_inline_keyboard()
    query.edit_message_reply_markup(reply_markup)

# Function to navigate to the previous page


def previous_page():
    global current_page
    current_page -= 1

# Function to navigate to the next page


def next_page():
    global current_page
    current_page += 1


# Create the updater and add the handlers
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add the handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(button_press))

# Start the bot
updater.start_polling()
