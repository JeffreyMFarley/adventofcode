import io

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes


# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        grid = []
        for line in f:
            row = [int(c) for c in line.strip()]
            grid.append(row)

    return grid

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    grid = load()

    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1

    lows = []
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            lowest = True
            if x > 0:
                lowest &= value < row[x-1]
            if x < max_x:
                lowest &= value < row[x+1]
            if y > 0:
                lowest &= value < grid[y-1][x]
            if y < max_y:
                lowest &= value < grid[y+1][x]

            if lowest:
                lows.append((y, x, value))

    print('\n'.join([f'({x},{y}) = {v}' for y,x,v in lows]))
    print(sum([v + 1 for _, _, v in lows]))

if __name__ == '__main__':
    main()
