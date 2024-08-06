from typing import Protocol

from sfish.game.cards import Card, CardSuit
from sfish.game.board import Board


class PlayerUI(Protocol):

    def get_move_from_user(self, player_cards: list[Card], valid_guesses: list[int], strong_suit: CardSuit) -> int:
        ...
        
    def get_guess_from_user(self, player_cards: list[Card], board: Board) -> Card:
        ...