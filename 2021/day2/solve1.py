import io

# ------------------------------------------------------

def main():
    with io.open('input1.txt','r', encoding='utf-8') as f:
        a = [l.split() for l in f]

    hpos = 0
    depth = 0

    for x in a:
        change = int(x[1])

        if x[0] == 'forward':
            hpos += change
        elif x[0] == 'down':
            depth += change
        elif x[0] == 'up':
            depth -= change
        else:
            print('Unknown command', x)

    print(hpos, depth, hpos * depth)

if __name__ == '__main__':
    main()
