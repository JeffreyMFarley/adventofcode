import io

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes

class Elf:
    def __init__(self) -> None:
        self.packs = []

    def __repr__(self) -> str:
        return ','.join([str(p) for p in self.packs])

    def add(self, pack: int) -> None:
        self.packs.append(pack)

    def holding(self) -> int:
        return sum(self.packs)

# ------------------------------------------------------
# Load

def load():
    elves = []
    with io.open(INPUT,'r', encoding='utf-8') as f:
        currElf = Elf()
        for l in f:
            s = l.strip()
            if not s:
               elves.append(currElf)
               currElf = Elf()
            else:
                currElf.add(int(s))

        elves.append(currElf)

    return elves    

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    elves = load()

    ordered = sorted([e.holding() for e in elves], reverse=True)

    print(f'Solution 1: {ordered[0]}')

    top_3 = ordered[0] + ordered[1] + ordered[2]
    print(f'Solution 2: {top_3}')


if __name__ == '__main__':
    main()
