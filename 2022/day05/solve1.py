import io
from copy import deepcopy
from dataclasses import dataclass

INPUT = "input1.txt"

# ------------------------------------------------------
# Classes


@dataclass
class Move:
    amount: int
    src: int
    dst: int


# ------------------------------------------------------
# Load


def read_chunks(s: str, n: int = 4) -> list[str]:
    N = len(s)
    return [s[i : i + n] for i in range(0, N, n)]


def load():
    # Read the separate areas
    with io.open(INPUT, "r", encoding="utf-8") as f:
        a, b = f.read().strip().split("\n\n")
    diagram = a.split("\n")

    # Process the stacks
    N_stacks = len(read_chunks(diagram.pop()))
    stacks = [[] for _ in range(N_stacks)]
    while len(diagram):
        level = read_chunks(diagram.pop())
        for i, box in enumerate(level):
            if box.strip():
                stacks[i].append(box[1:2])

    # Process the moves
    moves = []
    for x in b.split("\n"):
        s = x.split()
        moves.append(Move(int(s[1]), int(s[3]) - 1, int(s[5]) - 1))

    return stacks, moves


# ------------------------------------------------------
#


# ------------------------------------------------------
# Main


def main():
    stacks, moves = load()

    stacks2 = deepcopy(stacks)

    # make the CrateMover 9000 moves
    for move in moves:
        for i in range(move.amount):
            x = stacks[move.src].pop()
            stacks[move.dst].append(x)

    print("Solution 1:" + "".join([stk[-1] for stk in stacks]))

    # make the CrateMover 9001 moves
    for move in moves:
        temp = []
        for i in range(move.amount):
            temp.append(stacks2[move.src].pop())
        while len(temp):
            stacks2[move.dst].append(temp.pop())

    print("Solution 2:" + "".join([stk[-1] for stk in stacks2]))


if __name__ == "__main__":
    main()
