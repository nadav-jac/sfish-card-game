import random

from sfish.game.cards import Deck, Card, CardSuit
from sfish.game.player import Player
from sfish.game.board import Board

DEFAULT_SETS_IN_GAME = 10


class GameManager:
    """
    GameManager orchestrates the overall flow of the game, managing sets, players, and scoring.
    """

    def __init__(self, deck: Deck, board: Board, players: list[Player], total_sets: int = DEFAULT_SETS_IN_GAME):
        self.deck = deck
        self.board = board
        self.players = players
        self.total_sets = total_sets  # TODO: calc set in games by n players and max rank in def of cards?

    def run_game(self):
        """
        Executes the entire game across multiple sets, managing the flow and declaring results.
        """
        for current_set in range(1, self.total_sets + 1):
            self.start_set(current_set)
            self.run_set(current_set)
            self.end_set(current_set)
        self.announce_results()

    def start_set(self, current_set: int):
        """
        Prepares the deck, board, and players for a new set.

        Args:
            current_set (int): The index of the current set.
        """
        self.deck.reset()
        self.board.reset(strong_suit=select_strong_suit())
        for player in self.players:
            player.start_new_set()
        self.deal_cards(cards_per_player=current_set)
        self.collect_guesses(current_set)

    def deal_cards(self, cards_per_player: int):
        """
        Deals a specified number of cards to each player.

        Args:
            cards_per_player (int): Number of cards to be dealt to each player.
        """
        for player in self.players:
            player_hand = self.deck.draw_random_cards(count=cards_per_player)
            player.receive_cards(player_hand)

    def collect_guesses(self, current_set: int):
        """
        Collects guesses from each player on the number of hands they expect to win.

        Args:
            current_set (int): The index of the current set.
        """
        counter = 0
        guess_sum = 0
        for i in range(len(self.players)):
            counter += 1
            player = self.players[(current_set + i - 1) % len(self.players)]
            is_last_player = counter == current_set
            valid_guesses = self.calculate_valid_guesses(current_set, is_last_player, guess_sum)
            player.make_guess(strong_suit=self.board.strong_suit, possible_guesses=valid_guesses)
            guess_sum += player.current_guess
        assert guess_sum != current_set, "Sum of guesses should not equal the set index."

    def calculate_valid_guesses(self, current_set: int, is_last_player: bool, guess_sum: int) -> list[int]:
        """
        Calculates valid guesses for a player based on the current state of the game.

        Args:
            current_set (int): The index of the current set.
            is_last_player (bool): Whether the current player is the last to guess.
            guess_sum (int): Sum of guesses made by previous players.

        Returns:
            list[int]: A list of valid guesses for the player.
        """
        valid_guesses = list(range(current_set + 1))
        if is_last_player and guess_sum <= current_set:
            valid_guesses.remove(current_set - guess_sum)
        return valid_guesses

    def run_set(self, current_set: int):
        """
        Runs a complete set, allowing players to play all hands.

        Args:
            current_set (int): The index of the current set.
        """
        for _ in range(current_set):
            self.play_hand(current_set)
            hand_winner = self.board.hand_winner
            hand_winner.wins_in_set += 1

    def play_hand(self, current_set: int):
        """
        Conducts a single hand, allowing each player to play a card.

        Args:
            current_set (int): The index of the current set.
        """
        for i in range(len(self.players)):
            player = self.players[(current_set + i - 1) % len(self.players)]
            player.play_card(self.board)

    def end_set(self, current_set: int):
        """
        Finalizes the set, updating player scores based on their guesses and wins.

        Args:
            current_set (int): The index of the current set.
        """
        for player in self.players:
            player.score += calculate_points(current_set, player.current_guess, player.wins_in_set)

    def announce_results(self):
        """
        Announces the final results of the game.
        """
        pass


def calculate_points(current_set: int, guess: int, actual_wins: int) -> int:
    """
    Calculates points for a player based on their guess and actual wins.

    Args:
        current_set (int): The index of the current set.
        guess (int): The player's guess.
        actual_wins (int): The actual number of wins the player achieved.

    Returns:
        int: Points awarded to the player.
    """
    if guess == actual_wins:
        return current_set + guess
    else:
        return -abs(guess - actual_wins)


def select_strong_suit() -> CardSuit:
    """
    Randomly selects a strong suit for the current set.

    Returns:
        CardSuit: The selected strong suit.
    """
    random.choice(list(CardSuit))
