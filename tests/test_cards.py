import random
from sfish.game.cards import Card, CardSuit, Deck, N_SUITS


def test_deck_draw_random_cards_no_repeat():
    random.seed(0)
    deck = Deck(max_rank=2)
    assert len(deck.cards) == N_SUITS * 2
    first_drawn_cards = deck.draw_random_cards(N_SUITS)
    assert len(first_drawn_cards) == N_SUITS
    assert len(set(first_drawn_cards)) == N_SUITS
    assert len(deck.cards) == N_SUITS
    second_drawn_cards = deck.draw_random_cards(N_SUITS)
    assert len(second_drawn_cards) == N_SUITS
    assert len(set(second_drawn_cards)) == N_SUITS
    assert len(deck.cards) == 0
    assert len(set(first_drawn_cards + second_drawn_cards)) == N_SUITS * 2

