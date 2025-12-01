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
    print(f"The dial starts by pointing at {startPos}.")
    for line in data:
        direction = line[0]
        value = int(line[1:])
        
        skip_count = (startPos == 0)
        passed_zeros = value // 100
        value = value % 100

        if direction == 'L':
            startPos -= value
            while startPos < 0:
                if skip_count:
                    skip_count = False
                else:
                    passed_zeros += 1
                startPos += 100
        elif direction == 'R':
            startPos += value
            while startPos > 100:
                if skip_count:
                    skip_count = False
                else:
                    passed_zeros += 1
                startPos -= 100
        
        if startPos == 0:
            at_zero += 1
        if startPos == 100:
            startPos = 0
            at_zero += 1

        print(f"The dial is rotated {direction}{value} to point at {startPos}", end='')
        if passed_zeros > 0:
            at_zero += passed_zeros
            print(f"; during this rotation, it points at 0 {passed_zeros} times", end='')
        print(f".\t\t\t{at_zero}")

    return at_zero

# ------------------------------------------------------
# Main

def main():
    result = run()
    print(result)


if __name__ == '__main__':
    main()
