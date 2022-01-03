import io

# ------------------------

def convert(s):
    v = 0

    for c in s:
        v = v << 1
        if c == '1':
            v += 1

    return v


def partition_ties(a, index, tie_break):
    major = []
    minor = []
    for j, _ in enumerate(a):
        x = int(a[j][index])
        if x == tie_break:
            major.append(a[j])
        else:
            minor.append(a[j])

    return (major, minor) if tie_break else (minor, major)


def partition(a, index, tie_break):
    ones = []
    zeros = []
    for j, _ in enumerate(a):
        x = int(a[j][index])
        if x == 1:
            ones.append(a[j])
        else:
            zeros.append(a[j])

    if len(ones) == len(zeros):
        return partition_ties(a, index, tie_break)

    return (ones, zeros) if len(ones) > len(zeros) else (zeros, ones)


def main():
    with io.open('input1.txt','r', encoding='utf-8') as f:
        a = [l.strip() for l in f]

    width = len(a[0])
    index = 0

    o2, co2 = partition(a, index, 1)
    print(o2)
    print(co2)

    # Rounds
    while len(o2) > 1:
        index += 1
        o2, _ = partition(o2, index, 1)
        print(o2)

    oxy_rating = convert(o2[0])
    print(o2[0], oxy_rating)

    index = 0
    while len(co2) > 1:
        index += 1
        _, co2 = partition(co2, index, 0)
        print(co2)
    co2_rating = convert(co2[0])
    print(co2[0], co2_rating)

    print(oxy_rating * co2_rating)


if __name__ == '__main__':
    main()
