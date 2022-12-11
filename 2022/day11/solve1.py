import io

INPUT = 'input0.txt'

# ------------------------------------------------------
# Classes


# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        return [
            list(map(str.strip, x.splitlines()))
            for x in f.read().split('\n\n')
        ]

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    x = load()
    print(x)


if __name__ == '__main__':
    main()
