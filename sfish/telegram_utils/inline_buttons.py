from telegram import Update
from telegram.ext import ContextTypes

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data.split("|")
    action = data[0]

    if action == "play_card":
        card_played = data[1]  # The card the user selected
        user_id = query.from_user.id
        # Handle the player's move (connect to game logic)
        await query.edit_message_text(text=f"Card played: {card_played}")

    elif action == "make_guess":
        guess = int(data[1])  # The guess the user selected
        user_id = query.from_user.id
        # Handle the player's guess (connect to game logic)
        await query.edit_message_text(text=f"Guess made: {guess}")
