import io

INPUT = 'input0.txt'

# ------------------------------------------------------
# Classes


# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        return [l.strip() for l in f]

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    x = load()
    print(x)


if __name__ == '__main__':
    main()
