# inline_buttons.py

from telegram import Update
from telegram.ext import CallbackContext

def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    data = query.data.split("|")
    action = data[0]

    if action == "play_card":
        card_played = data[1]  # The card the user selected
        user_id = query.from_user.id
        # Handle the player's move (connect to game logic)
        query.edit_message_text(text=f"Card played: {card_played}")

    elif action == "make_guess":
        guess = int(data[1])  # The guess the user selected
        user_id = query.from_user.id
        # Handle the player's guess (connect to game logic)
        query.edit_message_text(text=f"Guess made: {guess}")
