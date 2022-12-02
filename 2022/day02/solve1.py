import io

INPUT = 'input1.txt'

DECODE_OPP = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS'
}

DECODE_RESP = {
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS'
}

SCORE_SHAPE = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3 
}

MATCH_WIN = 6
MATCH_DRAW = 3
MATCH_LOSE = 0

MATCHES = {
    ('ROCK', 'ROCK'): MATCH_DRAW,
    ('ROCK', 'PAPER'): MATCH_WIN,
    ('ROCK', 'SCISSORS'): MATCH_LOSE,
    ('PAPER', 'ROCK'): MATCH_LOSE,
    ('PAPER', 'PAPER'): MATCH_DRAW,
    ('PAPER', 'SCISSORS'): MATCH_WIN,
    ('SCISSORS', 'ROCK'): MATCH_WIN,
    ('SCISSORS', 'PAPER'): MATCH_LOSE,
    ('SCISSORS', 'SCISSORS'): MATCH_DRAW,
}

# ------------------------------------------------------
# Classes


class Round(object):
    def __init__(self, opponent: str, response: str) -> None:
        self.opponent = DECODE_OPP[opponent]
        self.response = DECODE_RESP[response]

    def __repr__(self) -> str:
        return f'{self.opponent} vs {self.response}'

    def score(self) -> int:
        return MATCHES[(self.opponent, self.response)] + SCORE_SHAPE[self.response] 


# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        return [Round(*(l.strip().split())) for l in f]

# ------------------------------------------------------
#

# ------------------------------------------------------
# Main

def main():
    rounds = load()
    results = [x.score() for x in rounds]

    print(sum(results))

if __name__ == '__main__':
    main()
