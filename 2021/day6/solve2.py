import io

INPUT = 'input1.txt'

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
    bins = [0] * (8+1)

    fish = load()
    for x in fish:
        bins[x] += 1

    print(sum(bins), ','.join(f'{x}' for x in bins))

    for day in range(256):
        a = bins[0]
        for i in range(1, 8 + 1):
            bins[i-1] = bins[i]
        bins[6] += a
        bins[8] = a
        # print(sum(bins), ','.join(f'{x}' for x in bins))

    print(sum(bins))


if __name__ == '__main__':
    main()
