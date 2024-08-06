
from sfish.game.cards import Card, CardSuit
from sfish.game.player import Player
from typing import List, Optional

class Board:
    """
    Board class manages the playing field for each hand within a set. 
    It tracks the cards played, the current strong suit, and determines the winner of each hand.
    """

    def __init__(self):
        self.strong_suit: Optional[CardSuit] = None
        self.played_cards: List[Card] = []
        self.played_by: List[Player] = []

    def reset(self, strong_suit: CardSuit):
        """
        Resets the board for a new set with the given strong suit.
        
        Args:
            strong_suit (CardSuit): The strong suit for the set.
        """
        self.strong_suit = strong_suit
        self.played_cards = []
        self.played_by = []

    def move(self, player: Player, card: Card):
        """
        Registers a player's move by adding their played card to the board.
        
        Args:
            player (Player): The player making the move.
            card (Card): The card being played.
        """
        self.played_cards.append(card)
        self.played_by.append(player)

    def determine_hand_winner(self) -> Optional[Player]:
        """
        Determines the winner of the current hand based on the played cards.
        
        Returns:
            Player: The player who won the hand.
        """
        leading_suit = self.played_cards[0].suit
        winning_card = self.played_cards[0]
        winning_player = self.played_by[0]

        for card, player in zip(self.played_cards[1:], self.played_by[1:]):
            if card.suit == winning_card.suit and card.rank > winning_card.rank:
                winning_card = card
                winning_player = player
            elif card.suit == self.strong_suit and (winning_card.suit != self.strong_suit or card.rank > winning_card.rank):
                winning_card = card
                winning_player = player

        self.played_cards = []
        self.played_by = []

        return winning_player

    @property
    def hand_winner(self) -> Optional[Player]:
        """
        Property to get the current hand's winner.

        Returns:
            Player: The player who won the hand.
        """
        return self.determine_hand_winner()