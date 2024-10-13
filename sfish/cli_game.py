from sfish.game.cards import Card, CardSuit, Deck, N_SUITS
from sfish.game.player import Player
from sfish.game.board import Board
from sfish.game.game_manager import GameManager, DEFAULT_SETS_IN_GAME
from sfish.user_interface.cli_ui import CLIPlayerUI

import logging


def main():
    # Initialize the game components
    logging.log(logging.INFO, "Starting a new game.")
    deck = Deck(max_rank=13)
    board = Board()
    players = [
        Player("Player 1", CLIPlayerUI("Player 1")),
        Player("Player 2", CLIPlayerUI("Player 2")),
        Player("Player 3", CLIPlayerUI("Player 3")),
        Player("Player 4", CLIPlayerUI("Player 4"))
    ]
    game_manager = GameManager(deck, board, players, total_sets=DEFAULT_SETS_IN_GAME)

    # Run the game
    game_manager.run_game()
    logging.log(logging.INFO, "Game over.")

if __name__ == "__main__":
    main()