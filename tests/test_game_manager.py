from sfish.game.game_manager import GameManager, calculate_points


def test_game_manager_init(mocker):
    deck = mocker.Mock()
    board = mocker.Mock()
    players = [mocker.Mock() for _ in range(4)]
    game_manager = GameManager(deck, board, players, total_sets=2)

def test_calculate_points():
    assert calculate_points(current_set=1, guess=1, actual_wins=1) == 2
    assert calculate_points(current_set=1, guess=1, actual_wins=0) == -1
    assert calculate_points(current_set=1, guess=0, actual_wins=1) == -1
    assert calculate_points(current_set=1, guess=0, actual_wins=0) == 1
    assert calculate_points(current_set=5, guess=3, actual_wins=1) == -2
    assert calculate_points(current_set=5, guess=3, actual_wins=3) == 8
