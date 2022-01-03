import io

from dataclasses import dataclass

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes

@dataclass
class Point:
    x: int
    y: int

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

@dataclass
class Low:
    x: int
    y: int
    z: int


class Basin:
    def __init__(self, grid, low):
        self.grid = grid
        self.low = low
        self.points = self.discover()

    def __str__(self):
        result = ''
        for y, row in enumerate(self.grid.grid):
            s = ''
            for x, value in enumerate(row):
                if x == self.low.x and y == self.low.y:
                    s += f'\033[4m{value:>2d}\033[0m '
                else:
                    s += f'{value:>2d} '
            result += s + '\n'

        return result

    @property
    def size(self):
        return len(self.points)

    def discover(self):
        grid = self.grid.grid
        max_x = self.grid.max_x
        max_y = self.grid.max_y

        def add_steps(q, x, y, points):
            if y > 0 and grid[y - 1][x] != 9:
                p = Point(x, y-1)
                if p not in points:
                    q.append(p)
            if y < max_y and grid[y + 1][x] != 9:
                p = Point(x, y+1)
                if p not in points:
                    q.append(p)
            if x > 0 and grid[y][x - 1] != 9:
                p = Point(x - 1, y)
                if p not in points:
                    q.append(p)
            if x < max_x and grid[y][x + 1] != 9:
                p = Point(x + 1, y)
                if p not in points:
                    q.append(p)

        points = set()
        queue = [Point(self.low.x, self.low.y)]

        while len(queue) > 0:
            point = queue.pop(0)
            points.add(point)
            add_steps(queue, point.x, point.y, points)

        return points


class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.max_y = len(grid) - 1
        self.max_x = len(grid[0]) - 1
        self.lows = self.find_lows()

    def __str__(self):
#        return '\033[4m{0:>2d}\033[0m'.format(self.value)
        return '\n'.join([f'({l.x},{l.y}) = {l.z}' for l in self.lows])

    def solution1(self):
        return sum([l.z + 1 for l in self.lows])

    def find_lows(self):
        lows = []
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                lowest = True
                if x > 0:
                    lowest &= value < row[x-1]
                if x < self.max_x:
                    lowest &= value < row[x+1]
                if y > 0:
                    lowest &= value < self.grid[y-1][x]
                if y < self.max_y:
                    lowest &= value < self.grid[y+1][x]

                if lowest:
                    lows.append(Low(x, y, value))
        return lows

# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        grid = []
        for line in f:
            row = [int(c) for c in line.strip()]
            grid.append(row)

    return Grid(grid)

# ------------------------------------------------------
# Main

def main():
    grid = load()

    # print(grid)
    # print(grid.solution1())

    basins = [Basin(grid, l) for l in grid.lows]
    ordered = sorted(basins, key=lambda x: x.size, reverse=True)

    sum = 1
    for b in ordered[0:3]:
        sum *= b.size

    print(sum)

if __name__ == '__main__':
    main()
