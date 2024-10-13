from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sfish.user_interface.player_ui import PlayerUI
    from sfish.game.cards import Card, CardSuit
    from sfish.game.board import Board  # Only import for type hints


class Player:
    """
    Player class represents a player in the game, managing their cards, guesses, and scores.
    """

    def __init__(self, name: str, player_ui: PlayerUI):
        self.name = name
        self.player_ui = player_ui
        self.score = 0
        self.current_guess = 0
        self.wins_in_set = 0
        self.hand: list[Card] = []

    def start_new_set(self):
        """
        Initializes player stats for a new set.
        """
        self.hand = []
        self.current_guess = 0
        self.wins_in_set = 0

    def receive_cards(self, new_cards: list[Card]):
        """
        Adds the given cards to the player's hand.

        Args:
            new_cards (list[Card]): Cards to be added to the player's hand.
        """        
        self.hand += new_cards

    def play_card(self, board: Board):
        """
        Allows the player to play a card, which is then removed from their hand.

        Args:
            board (Board): The game board where the card is played.
        """        
        card_to_play = self.player_ui.get_move_from_user(self.hand, board)
        self.hand.remove(card_to_play)
        board.move(self, card_to_play)

    def make_guess(self, strong_suit: CardSuit, possible_guesses: list[int]):
        """
        Allows the player to make a guess on the number of sets they expect to win.

        Args:
            strong_suit (CardSuit): The strong suit for the set.
            possible_guesses (list[int]): Valid guesses the player can make.
        """
        self.current_guess = self.player_ui.get_guess_from_user(self.hand, possible_guesses, strong_suit)
