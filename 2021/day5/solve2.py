import io
import math

from dataclasses import dataclass

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes

@dataclass
class Vector:
    x0: int
    y0: int
    x1: int
    y1: int

    def __str__(self):
        return f'{self.x0},{self.y0} -> {self.x1},{self.y1}'

    @staticmethod
    def parse(s):
        points = s.split(' -> ')
        start = points[0].split(',')
        end = points[1].split(',')
        return Vector(
            int(start[0]), int(start[1]),
            int(end[0]), int(end[1])
        )

    def points(self):
        if self.is_horiz():
            x0 = min(self.x0, self.x1)
            x1 = max(self.x0, self.x1)
            for x in range(x0, x1+1):
                yield x, self.y0

        elif self.is_vert():
            y0 = min(self.y0, self.y1)
            y1 = max(self.y0, self.y1)
            for y in range(y0, y1+1):
                yield self.x0, y

        else:
            x0 = min(self.x0, self.x1)
            x1 = max(self.x0, self.x1)
            y0 = min(self.y0, self.y1)
            y1 = max(self.y0, self.y1)

            steps = max(x1 - x0, y1 - y0)
            dirX = -1 if self.x0 > self.x1 else 1
            dirY = -1 if self.y0 > self.y1 else 1

            for i in range(steps + 1):
                yield self.x0 + (i * dirX), self.y0 + (i * dirY)

    def is_horiz(self):
        return self.y0 == self.y1

    def is_vert(self):
        return self.x0 == self.x1

    def maxes(self):
        return max(self.x0, self.x1), max(self.y0, self.y1)

    def slope(self):
        if self.x0 == self.x1:
            return math.nan

        return float(self.y1 - self.y0) / float(self.x1 - self.x0)


class Grid:
    def __init__(self, dimX, dimY):
        self.grid = [[0] * dimY for i in range(dimX)]

    def __str__(self):
        s = ''
        for row in self.grid:
            for col in row:
                s += ' . ' if col == 0 else f'{col:>2} '
            s += '\n'
        return s

    def add(self, x, y):
        try:
            self.grid[y][x] += 1
        except IndexError:
            print(f'({x}, {y}) is larger than {len(self.grid[0])}')
            raise

    def count_overlaps(self):
        total = 0
        for row in self.grid:
            for col in row:
                if col >= 2:
                    total += 1
        return total


# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        lines = [Vector.parse(l) for l in f]

    return lines

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    lines = load()

    dim = 0

    # Find the size of the grid
    for i, l in enumerate(lines):
        maxX, maxY = l.maxes()
        dim = max(maxX, maxY, dim)

    print(f'{dim} x {dim}')

    grid = Grid(dim + 1, dim + 1)
    for i, l in enumerate(lines):
        for x,y in l.points():
            grid.add(x,y)


    #print(grid)
    print(grid.count_overlaps())


if __name__ == '__main__':
    main()
