import io

INPUT = 'input1.txt'

SYNTAX = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

SCORE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
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
                return symb, stack

    return None, stack


def complete(stack):
    result = []
    score = 0

    while len(stack):
        symb = SYNTAX[stack.pop()]
        result.append(symb)

    for x in result:
        #print('\t', score, '=', score*5, '+', SCORE[x], '\t', x)
        score = score*5 + SCORE[x]

    return score

# ------------------------------------------------------
# Main

def main():
    chunks = load()

    scores = []

    for i, c in enumerate(chunks):
        invalid, stack = parse(c)
        if not invalid:
            scores.append(complete(stack))

    o_scored = list(sorted(scores))
    mid = len(o_scored) >> 1
    print(o_scored[mid])


if __name__ == '__main__':
    main()
