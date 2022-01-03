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
    vx += -1 if vx > 0 else 1
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
        for vx in range(4, 40)
        for vy in range(-5, 150)
    ]

    # vectors = [
    #     (0, 0, 7, 2),
    #     (0, 0, 6, 3),
    #     (0, 0, 9, 0),
    #     (0, 0, 17, -4),
    #     (0, 0, 6, 9)
    # ]

    winners = []
    for vector in vectors:
        max_y = 0
        result = None
        v = tuple(vector)
        while result is None:
            v = motion(v)
            max_y = max(v[1], max_y)
            if in_target(v, T0, T1):
                result = 1
            elif passed_target(v, T0, T1):
                result = 0

        if result:
            heapq.heappush(winners, (max_y, vector))

    z = heapq.nlargest(1, winners)
    print(z)

if __name__ == '__main__':
    main()
