import io
from dataclasses import dataclass
from typing import Type

INPUT = "input0.txt"


def sign(i: int) -> int:
    if i == 0:
        return 0
    elif i < 0:
        return -1
    return 1

# ------------------------------------------------------
# Classes


@dataclass
class Direction:
    dx: int
    dy: int

    def length(self):
        return abs(self.dx) + abs(self.dy)

    def is_diagonal(self):
        return self.dx != 0 and self.dy != 0


@dataclass
class Move:
    direction: Direction
    length: int


@dataclass
class Position:
    x: int
    y: int

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def copy(self):
        return Position(self.x, self.y)


@dataclass
class Vector:
    start: Position
    direction: Direction
    index: int

    def update(self, direction: Direction) -> None:
        self.start.x += direction.dx
        self.start.y += direction.dy
        self.direction = direction

    def distance(self, other) -> Direction:
        return Direction(
            self.start.x - other.start.x, self.start.y - other.start.y
        )

    def symbol(self) -> str:
        return 'H' if self.index == 0 else str(self.index)
        # if self.direction.dy == 0:
        #     return '<' if self.direction.dx < 0 else '>'
        # elif self.direction.dx == 0:
        #     return 'v' if self.direction.dy < 0 else '^'
        
        # return 'x'
        

DIR_MAP = {
    'L': Direction(-1, 0),
    'R': Direction(1, 0),
    'U': Direction(0, 1),
    'D': Direction(0, -1),
}


class Arena(object):
    def __init__(self, size=2) -> None:
        self.size = size
        self.rope = [Vector(Position(0, 0), Direction(0, 0), i) for i in range(size)]
        self.history = set()

    def __repr__(self) -> str:
        x0 = -12
        y0 = -12
        x1 = 12
        y1 = 12

        s = ''
        for y in range(y1 - 1, y0 - 1, -1):
            for x in range(x0, x1):
                curr = Position(x, y)
                knot = self.find_at(curr)
                
                if knot:
                    s += knot.symbol()
                elif x == 0 and y == 0:
                    s += 's'
                else:
                    s += '.'
            s += '\n'

        return s

    def find_at(self, pos:Position) -> Vector:
        for i in range(self.size):
            if self.rope[i].start == pos:
                return self.rope[i]

        return None

    def update(self, m: Move, detail=False) -> None:
        print('=' * 20)
        for i in range(m.length):
            if detail: print(' ')
            knot = self.rope[0]
            knot.update(m.direction)

            for i in range(1, self.size):
                prev = knot
                knot = self.rope[i]
                dist = prev.distance(knot)
                if dist.length() > 1:
                    if not dist.is_diagonal():
                        knot.update(prev.direction)
                    elif dist.length() > 2:
                        knot.update(Direction(sign(dist.dx), sign(dist.dy)))

            self.history.add(self.rope[-1].start.copy())
            if detail: print(self)
        if not detail: print(self)


# ------------------------------------------------------
# Load


def load():
    with io.open(INPUT, "r", encoding="utf-8") as f:
        return [
            Move(DIR_MAP[a], int(b))
            for a, b in map(str.split, f.read().splitlines())
        ]


# ------------------------------------------------------
#


# ------------------------------------------------------
# Main


def main():
    moves = load()

    arena = Arena(2)
    for m in moves:
        arena.update(m)
    print(f'Solution 1: {len(arena.history)}')

    # arena = Arena(10)
    # for i, m in enumerate(moves):
    #     arena.update(m, i == 2)
    # print(f'Solution 1: {len(arena.history)}')

if __name__ == "__main__":
    main()
