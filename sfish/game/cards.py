from enum import Enum
import random


class CardSuit(Enum):
    Diamond = "♦"
    Club = "♣"
    Heart = "♥"
    Spade = "♠"


N_SUITS = len(list(CardSuit))

class Card:
    def __init__(self, suit: CardSuit, rank):
        assert rank > 0, "Rank must be a positive integer."
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
    @classmethod
    def from_str(cls, card_str: str) -> "Card":
        pass




class Deck:
    """
    Deck class represents a deck of playing cards. It supports shuffling and dealing cards.
    """

    def __init__(self, max_rank: int = 13):
        assert max_rank > 0, "Max rank must be a positive integer."
        self.max_rank = max_rank
        self.cards = []  # Initialize with empty list
        self.reset()

    def draw_random_cards(self, count: int) -> list[Card]:
        """
        Draws a specified number of random cards from the deck.

        Args:
            count (int): Number of cards to draw.

        Returns:
            list[Card]: List of drawn cards.
        """
        assert 0 <= count <= len(self.cards), "Invalid number of cards to draw."
        drawn_cards = random.sample(self.cards, count)
        for card in drawn_cards:
            self.cards.remove(card)
        return drawn_cards

    def reset(self):
        """
        Resets the deck to contain a full set of cards.
        """
        self.cards = [
            Card(suit, rank) 
            for suit in list(CardSuit) 
            for rank in range(1, self.max_rank + 1)
        ]
