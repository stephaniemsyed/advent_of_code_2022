from enum import Enum


class RPSMove(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class RPSRoundWinner(Enum):
    PLAYER_ONE = 1
    PLAYER_TWO = 2
    DRAW = 3


class RPSRound:
    round_winner = 0
    player_one_score = 0
    player_two_score = 0

    def __init__(self, player_one_move: RPSMove, player_two_move: RPSMove):
        self.player_one_move = player_one_move
        self.player_two_move = player_two_move
        self._set_winner()
        self._set_score()

    def _set_winner(self):
        if self.player_one_move == RPSMove.ROCK:
            if self.player_two_move == RPSMove.ROCK:
                self.round_winner = RPSRoundWinner.DRAW
            elif self.player_two_move == RPSMove.PAPER:
                self.round_winner = RPSRoundWinner.PLAYER_TWO
            else:
                self.round_winner = RPSRoundWinner.PLAYER_ONE

        elif self.player_one_move == RPSMove.PAPER:
            if self.player_two_move == RPSMove.ROCK:
                self.round_winner = RPSRoundWinner.PLAYER_ONE
            elif self.player_two_move == RPSMove.PAPER:
                self.round_winner = RPSRoundWinner.DRAW
            else:
                self.round_winner = RPSRoundWinner.PLAYER_TWO
        else:
            if self.player_two_move == RPSMove.ROCK:
                self.round_winner = RPSRoundWinner.PLAYER_TWO
            elif self.player_two_move == RPSMove.PAPER:
                self.round_winner = RPSRoundWinner.PLAYER_ONE
            else:
                self.round_winner = RPSRoundWinner.DRAW

    def _set_score(self):
        player_one_round = 0
        player_two_round = 0
        if self.round_winner == RPSRoundWinner.PLAYER_ONE:
            player_one_round = 6
        elif self.round_winner == RPSRoundWinner.PLAYER_TWO:
            player_two_round = 6
        else:
            player_one_round = 3
            player_two_round = 3

        self.player_one_score = self.player_one_move.value + player_one_round
        self.player_two_score = self.player_two_move.value + player_two_round

    def round_winner(self) -> RPSRoundWinner:
        return self.round_winner


def parse_move(raw_input: str) -> RPSMove:
    letter = raw_input.strip()
    if letter == "A" or letter == "X":
        return RPSMove.ROCK
    elif letter == "B" or letter == "Y":
        return RPSMove.PAPER
    elif letter == "C" or letter == "Z":
        return RPSMove.SCISSORS
    else:
        raise Exception(f"Invalid player one input: \'{letter}\'")


def parse_round_by_letter(round_input: str) -> RPSRound:
    letters = round_input.split(" ")

    player_one_move = parse_move(letters[0])
    player_two_move = parse_move(letters[1])

    return RPSRound(player_one_move=player_one_move, player_two_move=player_two_move)


def parse_response_move(player_one_move: RPSMove, result: str):
    if result == "X":
        if player_one_move == RPSMove.ROCK:
            return RPSMove.SCISSORS
        elif player_one_move == RPSMove.PAPER:
            return RPSMove.ROCK
        elif player_one_move == RPSMove.SCISSORS:
            return RPSMove.PAPER
    elif result == "Y":
        return player_one_move
    elif result == "Z":
        if player_one_move == RPSMove.ROCK:
            return RPSMove.PAPER
        elif player_one_move == RPSMove.PAPER:
            return RPSMove.SCISSORS
        elif player_one_move == RPSMove.SCISSORS:
            return RPSMove.ROCK


def parse_round(round_input: str) -> RPSRound:
    letters = round_input.split()

    player_one_move = parse_move(letters[0])
    player_two_move = parse_response_move(player_one_move, letters[1])

    return RPSRound(player_one_move, player_two_move)
