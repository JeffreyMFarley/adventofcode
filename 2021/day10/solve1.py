import io

INPUT = 'input1.txt'

SYNTAX = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

SCORE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

# ------------------------------------------------------
# Classes


# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        return [l.strip() for l in f]

# ------------------------------------------------------
#

def parse(line):
    stack = []

    for symb in line:
        #print(symb, '\t', stack)
        if symb in SYNTAX:
            stack.append(symb)
        else:
            curr_open = stack.pop()
            if SYNTAX[curr_open] != symb:
                return symb

    return None


# ------------------------------------------------------
# Main

def main():
    chunks = load()

    sum = 0

    for i, c in enumerate(chunks):
        invalid = parse(c)
        if invalid:
            sum += SCORE[invalid]

    print(sum)


if __name__ == '__main__':
    main()
