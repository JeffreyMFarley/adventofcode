import io

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes


# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        s = f.read()
        return [int(x) for x in s.split(',')]

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    fish = load()
    output = ','.join([f'{x}' for x in fish])
    print(f'Initial State: {output}')

    for day in range(18):
        new_fish = 0
        for i, x in enumerate(fish):
            if x == 0:
                fish[i] = 6
                new_fish += 1
            else:
                fish[i] -= 1

        for c in range(new_fish):
            fish.append(8)
        # output = ','.join([f'{x}' for x in fish])
        # print(f'After {day + 1:>2} days: {output}')

    print(len(fish))



if __name__ == '__main__':
    main()
