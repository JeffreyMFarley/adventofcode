import io

INPUT = 'input1.txt'
COLS = 10
ROWS = 10


# ------------------------------------------------------
# Classes


class Cell:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = int(value)
        self.flash = False

    def __str__(self):
        if self.flash:
            return f'\033[1m0\033[0m'

        return f'\033[2m{self.value}\033[0m'

    @property
    def point(self):
        return self.x, self.y

    def increase(self):
        if self.value >= 9:
            self.flash = True
        elif self.value == 0:
            self.value += 1
            self.flash = False
        else:
            self.value += 1

    def reset(self):
        self.value = 0
        self.flash = False


class Grid:
    def __init__(self, dimX, dimY):
        self.grid = [[None] * dimY for i in range(dimX)]
        self.flashers = []
        self.total_flash = 0
        self.all_synched = False

    def __str__(self):
        s = ''
        for row in self.grid:
            for cell in row:
                s += str(cell)
            s += '\n'
        return s

    def add(self, x, y, v):
        try:
            self.grid[y][x] = Cell(x, y, v)
        except IndexError:
            print(f'({x}, {y}) is larger than {len(self.grid[0])}')
            raise

    def cell(self, x, y):
        if x < 0 or x >= COLS or y < 0 or y >= ROWS:
            return None

        return self.grid[y][x]

    def increment(self, cell):
        if cell and not cell.flash:
            cell.increase()
            if cell.flash:
                self.flashers.append(cell)

    def step(self):
        self.flashers = []

        # Increment
        for row in self.grid:
            for cell in row:
                if cell.flash:
                    cell.reset()
                self.increment(cell)

        # Handle flashers
        while len(self.flashers):
            src = self.flashers.pop(0)
            self.total_flash += 1
            x, y = src.point
            self.increment(self.cell(x - 1, y - 1))
            self.increment(self.cell(x, y - 1))
            self.increment(self.cell(x + 1, y - 1))
            self.increment(self.cell(x - 1, y))
            self.increment(self.cell(x + 1, y))
            self.increment(self.cell(x - 1, y + 1))
            self.increment(self.cell(x, y + 1))
            self.increment(self.cell(x + 1, y + 1))

        # Are they all on?
        self.all_synched = True
        for row in self.grid:
            for cell in row:
                self.all_synched &= cell.flash


# ------------------------------------------------------

def load():
    grid = Grid(COLS, ROWS)

    with io.open(INPUT,'r', encoding='utf-8') as f:
        for y, line in enumerate(f):
            for x, value in enumerate(line.strip()):
                grid.add(x, y, value)

    return grid

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    grid = load()

    print(grid)

    for i in range(270):
        grid.step()
        if grid.all_synched:
            print('After step', i + 1, grid.total_flash)
            print(grid)

    print(grid.total_flash)

if __name__ == '__main__':
    main()
