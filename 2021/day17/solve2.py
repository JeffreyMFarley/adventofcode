import heapq
import io

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes


# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        raw = f.read()
    _, _, sx, sy = raw.split()

    X = [int(x) for x in sx.strip('x=,').split('.') if x]
    Y = [int(y) for y in sy.strip('y=').split('.') if y]
    return (min(X), min(Y)), (max(X), max(Y))

# ------------------------------------------------------
#

def motion(vector):
    x, y, vx, vy = vector
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    vy -= 1
    return (x, y, vx, vy)

def in_target(v, t0, t1):
    return t0[0] <= v[0] <= t1[0] and t0[1] <= v[1] <= t1[1]

def passed_target(v, t0, t1):
    return v[0] > t1[0] or v[1] < t0[1]

# ------------------------------------------------------
# Main

def main():
    T0, T1 = load()

    vectors = [
        (0, 0, vx, vy)
        for vx in range(1, 2000)
        for vy in range(-2000, 2000)
    ]

    # vectors = [
    #     (0, 0, 5, 7),
    #     (0, 0, 7, 6),
    #     (0, 0, 7, 9),
    # ]

    winners = 0
    for vector in vectors:
        result = None
        v = tuple(vector)
        while result is None:
            v = motion(v)
            if in_target(v, T0, T1):
                result = 1
            elif passed_target(v, T0, T1):
                result = 0

        if result:
            winners += 1

    print(winners)
    # for w in sorted(winners):
    #     print(w)

if __name__ == '__main__':
    main()
