import io

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes

class CRT(object):
    def __init__(self, width:int=40, height:int=6) -> None:
        self.width = width
        self.height = height
        self.buffer = [
            ['.' for _ in range(width)]
            for _ in range(height)
        ]
        self.row = 0
        self.col = 0

    def __repr__(self) -> str:
        s = ''
        for y in range(self.height):
            for x in range(self.width):
                s += self.buffer[y][x]
            s += '\n'
        return s

    def draw(self, visible:bool):
        self.buffer[self.row][self.col] = '#' if visible else '.'

    def advance(self):
        self.col += 1
        if self.col >= self.width:
            self.col = 0
            self.row += 1
            if self.row >= self.height:
                self.row = 0


class CPU(object):
    def __init__(self, instructions) -> None:
        self.crt = CRT()
        self.X = 1
        self.cycle = 1
        self.instructions = instructions
        self.clear()

    def __repr__(self) -> str:
        s = ['.' for _ in range(self.crt.width)]
        s[self.X - 1] = '#'
        s[self.X] = '#'
        s[self.X + 1] = '#'
        return ''.join(s)

    def show_registers(self) -> str:
        return f'[{self.cycle}]\tX: {self.X}\tIP: {self.IP}\t AX:{self.AX}\tCX: {self.CX}'

    def cycle_start(self):
        if not self.IP:
            self.load_new_instruction()

        visible = self.X - 1 <= self.crt.col <= self.X + 1
        self.crt.draw(visible)

    def cycle_end(self):
        self.crt.advance()
        self.CX -= 1
        if self.CX <= 0:
            self.execute()
            self.clear()
        self.cycle += 1

    def load_new_instruction(self) -> None:
        s = self.instructions.pop(0)
        if s == 'noop':
            self.IP = 'Noop'
            self.AX = 0
            self.CX = 1
        else:
            self.IP, x = s.split()
            self.AX = int(x)
            self.CX = 2

    def execute(self) -> None:
        if self.IP == 'addx':
            self.X += self.AX

    def clear(self) -> None:
        self.IP = None
        self.AX = 0
        self.CX = 0

    @property
    def signal_strength(self) -> int:
        return self.cycle * self.X

# ------------------------------------------------------
# Load


def load():
    with io.open(INPUT, 'r', encoding='utf-8') as f:
        return f.read().splitlines()


# ------------------------------------------------------
#


# ------------------------------------------------------
# Main


def main():
    cpu = CPU(load())
    # cpu = CPU(['noop', 'addx 3', 'addx -5'])

    solution_1 = 0
    while len(cpu.instructions) or cpu.CX > 0:
        cpu.cycle_start()

        if cpu.cycle in [20, 60, 100, 140, 180, 220]:
            solution_1 += cpu.signal_strength

        cpu.cycle_end()

    print(f'Solution 1: {solution_1}')
    print('Solution 2\n')
    print(cpu.crt)

if __name__ == '__main__':
    main()
