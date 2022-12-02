import io

INPUT = 'input1.txt'

DECODE_OPP = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS'
}

DECODE_RESULT = {
    'X': 'LOSE',
    'Y': 'DRAW',
    'Z': 'WIN'
}

SCORE_SHAPE = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3 
}

SCORE_RESULT = {
    'WIN': 6,
    'DRAW': 3,
    'LOSE': 0
}

MATCHES = {
    ('ROCK', 'WIN'): 'PAPER',
    ('ROCK', 'DRAW'): 'ROCK',
    ('ROCK', 'LOSE'): 'SCISSORS',
    ('PAPER', 'WIN'): 'SCISSORS',
    ('PAPER', 'DRAW'): 'PAPER',
    ('PAPER', 'LOSE'): 'ROCK',
    ('SCISSORS', 'WIN'): 'ROCK',
    ('SCISSORS', 'DRAW'): 'SCISSORS',
    ('SCISSORS', 'LOSE'): 'PAPER',
}

# ------------------------------------------------------
# Classes


class Round(object):
    def __init__(self, opponent: str, result: str) -> None:
        self.opponent = DECODE_OPP[opponent]
        self.result = DECODE_RESULT[result]

    def __repr__(self) -> str:
        return f'{self.opponent} needs {self.result}'

    def score(self) -> int:
        return SCORE_SHAPE[
            MATCHES[(self.opponent, self.result)]
        ] + SCORE_RESULT[self.result] 


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
