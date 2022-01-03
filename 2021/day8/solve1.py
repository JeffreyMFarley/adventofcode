import io

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes


# ------------------------------------------------------
# Load

def load():
    result = []

    with io.open(INPUT,'r', encoding='utf-8') as f:
        for line in f:
            _, o = line.split(' | ')
            result.append(o.split())

    return result

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    outputs = load()

    accum = 0
    for row in outputs:
        for segment in row:
            x = len(segment)
            if x == 2 or x == 3 or x == 4 or x == 7:
                accum += 1

    print(accum)


if __name__ == '__main__':
    main()
