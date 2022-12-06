import io

INPUT = "input1.txt"

# ------------------------------------------------------
# Load


def load():
    with io.open(INPUT, "r", encoding="utf-8") as f:
        return f.read().splitlines()[0]


# ------------------------------------------------------
# Functions


def find_uniques(a: str, n: int) -> int:
    for i in range(len(a) - n + 1):
        s = set(a[i : i + n])
        if len(s) == n:
            return i + n


# ------------------------------------------------------
# Main


def main():
    signal = load()
    print(f"Solution 1: {find_uniques(signal, 4)}")
    print(f"Solution 2: {find_uniques(signal, 14)}")


if __name__ == "__main__":
    main()
