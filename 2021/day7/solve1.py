import io

INPUT = 'input0.txt'

# ------------------------------------------------------
# Classes


# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        s = f.read()
        return [int(x) for x in s.split(',')]

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    positions = load()
    N = max(positions)

    costs = [0] * (N + 1)

    for i in range(N + 1):
        for p in positions:
            costs[i] += abs(p - i)

    print(min(costs))

if __name__ == '__main__':
    main()
