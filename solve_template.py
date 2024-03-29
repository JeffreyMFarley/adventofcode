import io

INPUT = 'input0.txt'

# ------------------------------------------------------
# Classes


# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        return f.read().splitlines()

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    x = load()
    print(x)


if __name__ == '__main__':
    main()
