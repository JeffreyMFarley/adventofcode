import io

def main():
    with io.open('input1.txt','r', encoding='utf-8') as f:
        a = [int(l.strip()) for l in f]

    prev = None
    count = 0

    for x in a:
        if prev is not None:
            count += 1 if x > prev else 0
        prev = x

    print(count)

if __name__ == '__main__':
    main()
