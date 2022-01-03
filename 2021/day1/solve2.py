import io

def main():
    with io.open('input1.txt','r', encoding='utf-8') as f:
        a = [int(l.strip()) for l in f]

    windowed = [a[i] + a[i+1] + a[i+2] for i in range(len(a) - 2)]

    prev = None
    count = 0

    for x in windowed:
        if prev is not None:
            count += 1 if x > prev else 0
        prev = x

    print(count)

if __name__ == '__main__':
    main()
