import io

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes

class Panel:
    def __init__(self, inputs, outputs):
        self.panel = [''] * 10
        self.inputs = inputs
        self.outputs = outputs
        self.map_wires()

    def __str__(self):
        s = ''
        for i, x in enumerate(self.panel):
            s += f'[{i}]: {x}\n'
        s += '\n'
        return s

    def assign(self, index, v):
        self.panel[index] = set(v)

    def decode_output(self):
        accum = 0
        for v in self.outputs:
            accum = accum * 10 + self.find_match(v)
        return accum

    def find_match(self, v):
        v_set = set(v)
        for i, p in enumerate(self.panel):
            if v_set == p:
                return i

    def map_wires(self):
        fives = []
        sixes = []

        for v in self.inputs:
            if len(v) == 2:
                self.assign(1, v)
            elif len(v) == 3:
                self.assign(7, v)
            elif len(v) == 4:
                self.assign(4, v)
            elif len(v) == 5:
                fives.append(v)
            elif len(v) == 6:
                sixes.append(v)
            elif len(v) == 7:
                self.assign(8, v)

        for v in sixes:
            v_set = set(v)
            if len(self.panel[4] - v_set) == 0:
                self.assign(9, v)
            elif len(self.panel[7] - v_set) == 0:
                self.assign(0, v)
            else:
                self.assign(6, v)

        for v in fives:
            v_set = set(v)
            if len(self.panel[6] - v_set) == 1:
                self.assign(5, v)
            elif len(self.panel[1] - v_set) == 0:
                self.assign(3, v)
            else:
                self.assign(2, v)


# ------------------------------------------------------
# Load

def load():
    result = []

    with io.open(INPUT,'r', encoding='utf-8') as f:
        for line in f:
            i, o = line.split(' | ')
            result.append((i.split(), o.split()))

    return result

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    i_o = load()

    total = 0
    for row in i_o:
        p = Panel(row[0], row[1])
        total += p.decode_output()

    print(total)

if __name__ == '__main__':
    main()
