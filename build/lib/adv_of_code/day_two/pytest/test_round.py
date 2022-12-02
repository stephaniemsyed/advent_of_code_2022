import pytest

import pytest

from adv_of_code.day_two.models import RPSMove, RPSRoundWinner, parse_round, RPSRound


@pytest.mark.parametrize(
    ["round_text", "expected_p1", "expected_p2", "expected_winner"],
    [
        ("A X", RPSMove.ROCK, RPSMove.ROCK, RPSRoundWinner.DRAW),
        ("A Y", RPSMove.ROCK, RPSMove.PAPER, RPSRoundWinner.PLAYER_TWO),
        ("A Z", RPSMove.ROCK, RPSMove.SCISSORS, RPSRoundWinner.PLAYER_ONE),
        ("B X", RPSMove.PAPER, RPSMove.ROCK, RPSRoundWinner.PLAYER_ONE),
        ("B Y", RPSMove.PAPER, RPSMove.PAPER, RPSRoundWinner.DRAW),
        ("B Z", RPSMove.PAPER, RPSMove.SCISSORS, RPSRoundWinner.PLAYER_TWO),
        ("C X", RPSMove.SCISSORS, RPSMove.ROCK, RPSRoundWinner.PLAYER_TWO),
        ("C Y", RPSMove.SCISSORS, RPSMove.PAPER, RPSRoundWinner.PLAYER_ONE),
        ("C Z", RPSMove.SCISSORS, RPSMove.SCISSORS, RPSRoundWinner.DRAW),
    ]
)
def test_round_parse(round_text: str, expected_p1, expected_p2, expected_winner):
    result = parse_round(round_text)
    assert result.player_one_move == expected_p1
    assert result.player_two_move == expected_p2
    assert result.round_winner == expected_winner

@pytest.mark.parametrize(
    ["p1_move", "p2_move", "p1_score", "p2_score"],
    [
        (RPSMove.ROCK, RPSMove.ROCK, 4, 4),
        (RPSMove.ROCK, RPSMove.PAPER, 1, 8),
        (RPSMove.ROCK, RPSMove.SCISSORS, 7, 3),
        (RPSMove.PAPER, RPSMove.ROCK, 8, 1),
        (RPSMove.PAPER, RPSMove.PAPER, 5, 5),
        (RPSMove.PAPER, RPSMove.SCISSORS, 2, 9),
        (RPSMove.SCISSORS, RPSMove.ROCK, 3, 7),
        (RPSMove.SCISSORS, RPSMove.PAPER, 9, 2),
        (RPSMove.SCISSORS, RPSMove.SCISSORS, 6, 6),
    ]
)
def test_round_score(p1_move: RPSMove, p2_move: RPSMove, p1_score: int, p2_score: int):
    result = RPSRound(p1_move, p2_move)
    assert result.player_one_score == p1_score
    assert result.player_two_score == p2_score
