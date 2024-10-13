import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from sfish.game.cards import Deck
from sfish.game.board import Board
from sfish.game.game_manager import GameManager
from sfish.game.player import Player
from sfish.user_interface.telegram_player_ui import TelegramPlayerUI
from sfish.telegram_utils.inline_buttons import button_callback


# Store game sessions by chat ID
active_games = {}
pending_players = {}

# Function to start a new game
def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    if chat_id in active_games:
        update.message.reply_text("A game is already in progress in this chat.")
    else:
        pending_players[chat_id] = []
        update.message.reply_text("Game created. Waiting for players to join with /join.")


# Function for players to join the game
def join(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    username = update.message.from_user.first_name

    if chat_id not in pending_players:
        update.message.reply_text("No active game to join. Start one with /start.")
    else:
        if user_id not in [p["user_id"] for p in pending_players[chat_id]]:
            pending_players[chat_id].append({"user_id": user_id, "name": username})
            update.message.reply_text(f"{username} has joined the game.")
        else:
            update.message.reply_text(f"{username}, you have already joined the game.")

        # If enough players have joined, start the game
        if len(pending_players[chat_id]) >= 4:
            start_game(update, context)


def start_game(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    if len(pending_players[chat_id]) < 4:
        update.message.reply_text("Not enough players to start the game.")
        return

    # Create player objects
    players = [
        Player(player["name"], TelegramPlayerUI(player["user_id"], context.bot))
        for player in pending_players[chat_id]
    ]

    # Initialize Deck, Board, and GameManager
    deck = Deck()
    board = Board()
    game_manager = GameManager(deck, board, players)

    # Store the game in active_games
    active_games[chat_id] = game_manager

    # Run the first set
    update.message.reply_text("All players have joined. The game is starting!")
    game_manager.run_game()  # Run the full game logic


def main():
    # Set up the Telegram bot
    telegram_bot_token = os.getenv("SFISH_TELEGRAM_BOT_TOKEN")
    updater = Updater(telegram_bot_token)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("join", join))

    # Add inline button handler (callback queries)
    dispatcher.add_handler(CallbackQueryHandler(button_callback))

    # Start polling
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
