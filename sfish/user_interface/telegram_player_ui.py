from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from sfish.game.cards import Card
from sfish.game.board import Board
from telegram.ext import ContextTypes

class TelegramPlayerUI:
    def __init__(self, user_id, bot):
        self.user_id = user_id
        self.bot = bot

    async def get_move_from_user(self, player_cards: list[Card], board: Board):
        """
        Prompts the user to choose a card to play using inline buttons.
        """
        card_buttons = []
        for card in player_cards:
            card_buttons.append([InlineKeyboardButton(text=str(card), callback_data=f"play_card|{str(card)}")])

        # Send the message with inline buttons
        reply_markup = InlineKeyboardMarkup(card_buttons)
        await self.bot.send_message(chat_id=self.user_id, text="Choose a card to play:", reply_markup=reply_markup)

    async def get_guess_from_user(self, player_cards: list[Card], possible_guesses: list[int], strong_suit: Card):
        """
        Prompts the user to make a guess using inline buttons.
        """
        guess_buttons = []
        for guess in possible_guesses:
            guess_buttons.append([InlineKeyboardButton(text=str(guess), callback_data=f"make_guess|{guess}")])

        # Send the message with inline buttons
        reply_markup = InlineKeyboardMarkup(guess_buttons)
        await self.bot.send_message(chat_id=self.user_id, text=f"Strong suit: {strong_suit}. How many sets will you win?", reply_markup=reply_markup)
