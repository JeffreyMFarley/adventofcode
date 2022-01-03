import io

from collections import Counter

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes

class Image(object):
    def __init__(self, input, iea, default):
        self.iea = iea
        self.input = input
        self.maxX, self.maxY = map(max, zip(*input))
        self.default = default

    def __str__(self):
        s = ''
        for y in range(-5, self.maxY + 6):
            for x in range(-5, self.maxX + 6):
                s += self.input.get((x, y), self.default)
            s += '\n'

        return s

    def sum_neighbors(self, x, y):
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
            c = self.input.get((x0, y0), self.default)
            v = int(c == '#')
            accum = (accum << 1) + v

        return accum

    def enhance(self):
        output = {}
        for y in range(-3, self.maxY + 3):
            for x in range(-3, self.maxX + 3):
                idx = self.sum_neighbors(x, y)
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

    return Image(input, iea, '.')


# ------------------------------------------------------
#

# ------------------------------------------------------
# Main

def main():
    image = load()

    print(image)
    i1 = Image(image.enhance(), image.iea, '#')
    print(i1)
    i2 = Image(i1.enhance(), image.iea, '.')
    print(i2)
    print(i2.solution1()) # 5647


if __name__ == '__main__':
    main()
