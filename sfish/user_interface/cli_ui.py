from sfish.game.cards import Card, CardSuit
from sfish.game.board import Board


class CLIPlayerUI:

    def get_move_from_user(self, player_cards: list[Card], board: Board) -> Card:
        return get_move_from_user(player_cards, board)

    def get_guess_from_user(self, player_cards: list[Card], valid_guesses: list[int], strong_suit: CardSuit) -> int:
        return get_guess_from_user(player_cards, valid_guesses, strong_suit)


def get_guess_from_user(player_cards: list[Card], valid_guesses: list[int], strong_suit: CardSuit) -> int:
    print(f"Your turn to guess! How many hands you will win in this set? \n " \
          f"Your cards are {player_cards} (overall {len(player_cards)} cards). and the strong suit is {strong_suit}.")
    answered_guess = get_int_from_user()
    while answered_guess not in valid_guesses:
        answered_guess = get_int_from_user()
    return answered_guess


def get_int_from_user() -> int:
    answer = input(f"Your turn to guess! How many hands you will win in this set?")
    while not answer.isdigit():
        answer = input(f"Can't parse your answer as a valid guess. Try again (your answer should contains only digits)")
    return answer


def get_move_from_user(player_cards: list[Card], board: Board) -> Card:
    answered_card = get_card_from_user(player_cards, board)
    while not is_valid_move(answered_card, player_cards, board.hand_suit):
        answered_card = get_card_from_user(player_cards, board)
    return answered_card


def get_card_from_user(player_cards: list[Card], board: Board) -> Card:
    answer = input(f"Pick your move! \n Your cards: {player_cards} \n The board state is {board.state} \n " \
                   f"The hand's suit is {board.hand_suit}; The strong suit is {board.strong_suit}.")
    answered_card = Card.from_str(answer)
    while answered_card is None:
        answer = input("Can't parse your answer as a valid card. Try again (your answer should be 'SUIT RANK').")
        answered_card = Card.from_str(answer)
    return answered_card


def is_valid_move(card_to_play: Card, player_cards: list[Card], hand_suit: CardSuit) -> bool:
    is_player_card = card_to_play in player_cards
    is_valid_suit = (card_to_play.suit == hand_suit) or (hand_suit not in {card.suit for card in player_cards})
    return is_player_card and is_valid_suit