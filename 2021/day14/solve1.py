import io

from collections import Counter

INPUT = 'input0.txt'

# ------------------------------------------------------
# Classes


# ------------------------------------------------------
# Load

def load():
    rules = {}

    with io.open(INPUT,'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            line = line.strip()
            if i == 0:
                template = line
            elif len(line):
                pair, insertion = line.split(' -> ')
                rules[(pair[0], pair[1])] = insertion

    return template, rules

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    template, rules = load()

    # print(template)
    # print('\n'.join([f'{k}: {v}' for k,v in rules.items()]))

    # Generate
    for j in range(10):
        ng = ''
        for i in range(len(template) - 1):
            pair = (template[i], template[i + 1])
            ng += pair[0] + rules[pair]
        template = ng + template[-1]

    # Tabulate
    c = Counter(template)
    ordered = c.most_common()
    print(ordered[0][1] - ordered[-1][1])


if __name__ == '__main__':
    main()
