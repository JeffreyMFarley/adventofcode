import io

from itertools import cycle

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes


# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        starting_pos = [int(line.strip().split(':')[1]) for line in f]

    return starting_pos

# ------------------------------------------------------
#

def new_position(old_pos, roll1, roll2, roll3):
    new_pos = (old_pos + roll1 + roll2 + roll3) % 10
    return 10 if new_pos == 0 else new_pos

# ------------------------------------------------------
# Main

def main():
    positions = load()
    scores = [0] * len(positions)

    dice_roll = cycle(range(1, 101))
    players = cycle([0, 1])
    roll_count = 0
    def rolls():
        return next(dice_roll), next(dice_roll), next(dice_roll)

    won = False
    while not won:
        player = next(players)
        roll1, roll2, roll3 = rolls()
        roll_count += 3

        positions[player] = new_position(positions[player], roll1, roll2, roll3)
        scores[player] += positions[player]
        won |= scores[player] >= 1000
        # print(f'Player {player + 1} rolls {roll1}+{roll2}+{roll3}', end=' ')
        # print(f'and moves to space {positions[player]}', end=' ')
        # print(f'for a total score of {scores[player]}.')

    print(min(*scores), roll_count, min(*scores) * roll_count)


if __name__ == '__main__':
    main()
