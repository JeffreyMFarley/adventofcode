import io
from functools import reduce

INPUT = "input1.txt"

# ------------------------------------------------------
# Load


def load():
    with io.open(INPUT, "r", encoding="utf-8") as f:
        return [l.strip() for l in f]


# ------------------------------------------------------
# Functiony functions


def find_common(t):
    intersect = reduce(lambda x, y: x & y, t)
    assert len(intersect) == 1
    return intersect.pop()


def partition_in_3(l):
    n = len(l)
    assert n % 3 == 0
    return [(set(l[i]), set(l[i + 1]), set(l[i + 2])) for i in range(0, n, 3)]


def prioritize(c) -> int:
    if c.islower():
        return ord(c[0]) - ord("a") + 1

    return ord(c[0]) - ord("A") + 27


def to_sets(s: str) -> tuple:
    n = len(s)
    assert n % 2 == 0
    mid = n >> 1
    return (set(s[:mid]), set(s[mid:]))


# ------------------------------------------------------
# Main


def main():
    packs = load()

    solution1 = sum(map(prioritize, map(find_common, map(to_sets, packs))))
    print(f"Solution 1:\t{solution1}")

    solution2 = sum(map(prioritize, map(find_common, partition_in_3(packs))))
    print(f"Solution 2:\t{solution2}")


if __name__ == "__main__":
    main()
