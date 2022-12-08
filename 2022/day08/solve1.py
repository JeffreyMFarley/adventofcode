import io

INPUT = "input1.txt"

# ------------------------------------------------------
# Load


def load():
    with io.open(INPUT, "r", encoding="utf-8") as f:
        grid = {}
        for y, line in enumerate(f):
            for x, w in enumerate(line.strip()):
                grid[(x, y)] = int(w)

    return grid, x + 1, y + 1


# ------------------------------------------------------
# Functions


def is_visible(grid, x: int, y: int, dim_x: int, dim_y: int) -> bool:
    height = grid[(x, y)]

    left = [grid[(xx, y)] >= height for xx in range(x)]
    right = [grid[(xx, y)] >= height for xx in range(x + 1, dim_x)]
    up = [grid[(x, yy)] >= height for yy in range(y)]
    down = [grid[(x, yy)] >= height for yy in range(y + 1, dim_y)]

    return not any(left) or not any(right) or not any(up) or not any(down)


def scenic_score(grid, x: int, y: int, dim_x: int, dim_y: int) -> int:
    height = grid[(x, y)]

    left, right, up, down = 0, 0, 0, 0

    for yy in range(y - 1, -1, -1):
        up += 1
        if grid[(x, yy)] >= height:
            break

    for xx in range(x - 1, -1, -1):
        left += 1
        if grid[(xx, y)] >= height:
            break

    for xx in range(x + 1, dim_x):
        right += 1
        if grid[(xx, y)] >= height:
            break

    for yy in range(y + 1, dim_y):
        down += 1
        if grid[(x, yy)] >= height:
            break

    return left * right * up * down


# ------------------------------------------------------
# Main


def main():
    grid, dim_x, dim_y = load()

    solution1 = sum(
        [
            is_visible(grid, x, y, dim_x, dim_y)
            for y in range(dim_y)
            for x in range(dim_x)
        ]
    )

    print(f"Solution 1: {solution1}")

    solution2 = max(
        [
            scenic_score(grid, x, y, dim_x, dim_y)
            for y in range(dim_y)
            for x in range(dim_x)
        ]
    )
    print(f"Solution 2: {solution2}")


if __name__ == "__main__":
    main()
