import io

from collections import Counter

INPUT = 'input1.txt'

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
                rules[pair[0] + pair[1]] = insertion

    return template, rules

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    template, rules = load()

    # print(template)
    # print('\n'.join([f'{k}: {v}' for k,v in rules.items()]))
    char_counter = Counter(template)
    pair_counter = Counter()
    size = len(template)

    for i in range(size - 1):
        pair = template[i] + template[i + 1]
        pair_counter[pair] += 1
    # print(pair_counter, char_counter)

    # Generate
    for j in range(40):
        this_step = Counter()
        for pair, freq in pair_counter.items():
            insertion = rules[pair]
            this_step[pair[0] + insertion] += freq
            this_step[insertion + pair[1]] += freq
            char_counter[insertion] += freq
        size += size - 1
        pair_counter = this_step
        print(f'{j + 1:>2d}: {size:>17,d}')

    # Tabulate
    ordered = char_counter.most_common()
    print(f'{ordered[0][1]}\t{ordered[-1][1]}\t{ordered[0][1] - ordered[-1][1]}')


if __name__ == '__main__':
    main()
