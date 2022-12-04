import io

INPUT = "input1.txt"

# ------------------------------------------------------
# Load


def load():
    with io.open(INPUT, "r", encoding="utf-8") as f:
        return f.read().splitlines()


# ------------------------------------------------------
# Functions


def fully_contains(t: tuple[tuple[int, int], tuple[int, int]]) -> int:
    a, b = t
    if a[0] >= b[0] and a[1] <= b[1]:
        return 1

    if b[0] >= a[0] and b[1] <= a[1]:
        return 1

    return 0


def overlaps(t: tuple[tuple[int, int], tuple[int, int]]) -> int:
    a, b = t

    if a[1] < b[0]:
        return 0

    if b[1] < a[0]:
        return 0

    return 1


def parse(s: str) -> tuple[tuple[int, int], tuple[int, int]]:
    a_sections, b_sections = s.split(",")
    return (
        tuple(map(int, a_sections.split("-"))),
        tuple(map(int, b_sections.split("-"))),
    )


# ------------------------------------------------------
# Main


def main():
    lines = load()

    section_ids = list(map(parse, lines))
    solution_1 = sum(map(fully_contains, section_ids))
    solution_2 = sum(map(overlaps, section_ids))

    print(f"Solution 1: {solution_1}")
    print(f"Solution 2: {solution_2}")


if __name__ == "__main__":
    main()
