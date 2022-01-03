import io

from collections import Counter

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes

class Image(object):
    def __init__(self, input, iea):
        self.iea = iea
        self.input = input
        self.minX, self.minY = map(min, zip(*input))
        self.maxX, self.maxY = map(max, zip(*input))

    def __str__(self):
        s = f'({self.minX}, {self.minY}) - ({self.maxX},{self.maxY})\n'
        for y in range(self.minY - 5, self.maxY + 6):
            for x in range(self.minX - 5, self.maxX + 6):
                s += self.input.get((x, y), '.')
            s += '\n'

        return s

    def sum_neighbors(self, x, y, default):
        coords = [
            (x - 1, y - 1),
            (x, y -1),
            (x + 1, y - 1),
            (x - 1, y),
            (x, y),
            (x + 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
        ]

        accum = 0
        for x0, y0 in coords:
            c = self.input.get((x0, y0), default)
            v = int(c == '#')
            accum = (accum << 1) + v

        return accum

    def enhance(self, default):
        output = {}
        for y in range(self.minY - 3, self.maxY + 4):
            for x in range(self.minX - 3, self.maxX + 4):
                idx = self.sum_neighbors(x, y, default)
                output[(x,y)] = self.iea[idx]
                # print(f'({x}, {y}) => {idx} {self.iea[idx]}')
        return output


    def solution1(self):
        ctr = Counter(list(self.input.values()))
        return ctr['#']

# ------------------------------------------------------
# Load

def load():
    input = {}

    with io.open(INPUT,'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i == 0:
                iea = [c for c in line.strip()]
            elif i > 1:
                y = i - 2
                for x, c in enumerate(line.strip()):
                    input[(x, y)] = c

    return Image(input, iea)


# ------------------------------------------------------
#

# ------------------------------------------------------
# Main

def main():
    image = load()

    print(image)
    for i in range(50):
        image = Image(image.enhance('#' if (i & 1) else '.'), image.iea)
        print(i)

    print(image.solution1()) # 15653


if __name__ == '__main__':
    main()
