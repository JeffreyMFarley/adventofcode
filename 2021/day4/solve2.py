import io

INPUT = 'input1.txt'
COLS = 5
ROWS = 5

class Cell:
    def __init__(self, value, called=False):
        self.value = value
        self.called = called

    def __str__(self):
        if self.called:
            return '\033[4m{0:>2d}\033[0m'.format(self.value)

        return f'{self.value:>2d}'

# ------------------------------------------------------

def load():
    boards = []

    with io.open(INPUT,'r', encoding='utf-8') as f:
        raw = f.readlines()

    # Get the numbes
    numbers = [int(x) for x in raw.pop(0).split(',')]

    # Get the boards
    while len(raw):
        # Blank line
        raw.pop(0)

        board = []
        for r in range(ROWS):
            board.append([Cell(int(x), False) for x in raw.pop(0).split()])
        boards.append(board)

    return numbers, boards

# ------------------------------------------------------

def update_board(b, current):
    for row in b:
        for cell in row:
            if cell.value == current:
                cell.called = True
                return


def scan_board(b):
    # Check rows
    for row in b:
        winner = True
        for cell in row:
            winner &= cell.called
        if winner:
            return True

    # Check columns
    for col in range(COLS):
        winner = True
        for row in b:
            winner &= row[col].called
        if winner:
            return True


    return False


def score_board(b):
    total = 0
    for row in b:
        for cell in row:
            if not cell.called:
                total += cell.value
    return total


def print_board(i, b):
    print(i)
    for row in b:
        s = ''
        for cell in row:
            s += str(cell) + ' '
        print(s)
    print('\n')

# ------------------------------------------------------

def main():
    numbers, boards = load()
    print(numbers)

    winners = set()
    last = None
    current = None

    while len(numbers) and len(winners) < len(boards):
        current = numbers.pop(0)

        print('{}{}{}{}'.format('='*10, current, '='*10, len(boards)))

        for i, b in enumerate(boards):
            if i in winners:
                continue

            update_board(b, current)
            if scan_board(b):
                print_board(i, b)
                last = b
                winners.add(i)

    print_board(100, last)
    print(score_board(last) * current)



if __name__ == '__main__':
    main()
