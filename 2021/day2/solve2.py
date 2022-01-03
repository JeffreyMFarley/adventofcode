import io

# ------------------------------------------------------

def main():
    with io.open('input1.txt','r', encoding='utf-8') as f:
        a = [l.split() for l in f]

    hpos = 0
    depth = 0
    aim = 0

    for i, x in enumerate(a):
        change = int(x[1])

        if x[0] == 'forward':
            hpos += change
            depth += change * aim
        elif x[0] == 'down':
            aim += change
        elif x[0] == 'up':
            aim -= change
        else:
            print('Unknown command', x)

        print(i, hpos, depth, aim)

    print(hpos, depth, hpos * depth)

if __name__ == '__main__':
    main()
