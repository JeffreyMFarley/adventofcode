import io

from itertools import product

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes

class Step(object):
    def __init__(self, line):
        def splitrange(s):
            _, r = s.split('=')
            return [int(x) for x in r.split('.') if x]

        self.turn, remain = line.strip().split(' ')
        xr, yr, zr = remain.split(',')
        self.x0, self.xN = splitrange(xr)
        self.y0, self.yN = splitrange(yr)
        self.z0, self.zN = splitrange(zr)

        # Fix ranges
        self.x0 = max(-50, self.x0)
        self.xN = min(self.xN, 50)
        self.y0 = max(-50, self.y0)
        self.yN = min(self.yN, 50)
        self.z0 = max(-50, self.z0)
        self.zN = min(self.zN, 50)

    def __repr__(self):
        return f'{self.turn} {self.x0}..{self.xN}, {self.y0}..{self.yN}\n'

    def __iter__(self):
        return product(
            range(self.x0, self.xN + 1),
            range(self.y0, self.yN + 1),
            range(self.z0, self.zN + 1)
        )

    def inbounds(self, x, y, z):
        return (
            -50 <= x <= 50 and
            -50 <= y <= 50 and
            -50 <= z <= 50
        )

    def execute(self, cuboid):
        if self.turn == 'on':
            for x,y,z in iter(self):
                cuboid.add((x,y,z))
        else:
            for x,y,z in iter(self):
                if (x,y,z) in cuboid:
                    cuboid.remove((x,y,z))


# ------------------------------------------------------
# Load

def load():

    with io.open(INPUT,'r', encoding='utf-8') as f:
        steps = [Step(l) for l in f]

    return steps

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    steps = load()
    print(steps)

    cuboid = set()

    for step in steps:
        step.execute(cuboid)

    print(len(cuboid))


if __name__ == '__main__':
    main()
