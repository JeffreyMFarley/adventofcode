import io

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes


# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        return f.read().splitlines()

# ------------------------------------------------------
#

def run():
    startPos = 50
    at_zero = 0

    data = load()
    for line in data:
        direction = line[0]
        value = int(line[1:])
        if direction == 'L':
            startPos -= value
            while startPos < 0:
                startPos += 100
        elif direction == 'R':
            startPos += value
            while startPos >= 100:
                startPos -= 100
        
        if startPos == 0:
            at_zero += 1

    return at_zero

# ------------------------------------------------------
# Main

def main():
    result = run()
    print(result)


if __name__ == '__main__':
    main()
