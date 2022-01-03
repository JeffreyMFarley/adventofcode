import io
import heapq

from math import *

INPUT = 'input1.txt'

SCAN_RANGE = 1000

# ------------------------------------------------------

orientations = [
    lambda x, y, z: (x, y, z),          #  0 original face
    lambda x, y, z: (x, z, -1*y),       #  1 rotate 90 x
    lambda x, y, z: (x, -1*y, -1*z),    #  2 rotate 180 x
    lambda x, y, z: (x, -1*z, y),       #  3 rotate 270 x
    lambda x, y, z: (-1*x, -1*y, z),    #  4 rotate 180 z
    lambda x, y, z: (-1*x, -1*z, -1*y), #  5 rotate 180 z rotate 90 x
    lambda x, y, z: (-1*x, y, -1*z),    #  6 rotate 180 z rotate 180 x
    lambda x, y, z: (-1*x, z, y),       #  7 rotate 180 z rotate 270 x
    lambda x, y, z: (-1*y, x, z),       #  8 rotate 270 z
    lambda x, y, z: (-1*y, z, -1*x),    #  9 rotate 270 z rotate 90 y
    lambda x, y, z: (-1*y, -1*x, -1*z), # 10 rotate 270 z rotate 180 y
    lambda x, y, z: (-1*y, -1*z, x),    # 11 rotate 270 z rotate 270 y
    lambda x, y, z: (y, -1*x, z),       # 12 rotate 90 z
    lambda x, y, z: (y, z, x),          # 13 rotate 90 z rotate 270 y
    lambda x, y, z: (y, x, -1*z),       # 14 rotate 90 z rotate 180 y
    lambda x, y, z: (y, -1*z, -1*x),    # 15 rotate 90 z rotate 90 y
    lambda x, y, z: (z, x, y),          # 16 rotate 90 y rotate 270 z
    lambda x, y, z: (z, y, -1*x),       # 17 rotate 90 y
    lambda x, y, z: (z, -1*x, -1*y),    # 18 rotate 90 y rotate 90 z
    lambda x, y, z: (z, -1*y, x),       # 19 rotate 90 y rotate 180 z
    lambda x, y, z: (-1*z, -1*x, y),    # 20 rotate 270 y rotate 90 z
    lambda x, y, z: (-1*z, -1*y, -1*x), # 21 rotate 270 y rotate 180 z
    lambda x, y, z: (-1*z, x, -1*y),    # 22 rotate 270 y rotate 270 z
    lambda x, y, z: (-1*z, x, y),       # 23 rotate 270 y
]

# ------------------------------------------------------
# Vectors

def match_orientation(a, b):
    best = 0

    for i, fn in enumerate(orientations):
        test_orient = {fn(*v) for v in b}
        for target in a:
            for source in test_orient:
                offset = vector_minus(target,source)
                testSet = {vector_add(vec,offset) for vec in test_orient}
                overlap = len(a.intersection(testSet))
                if overlap >= 12:
                    return i, offset
                else:
                    best = max(best, overlap)

    return None, None


def orient_vectors(vectors, idx, offset):
    return {vector_add(orientations[idx](*v), offset) for v in vectors}


def vector_add(a,b):
    i,j,k = a
    x,y,z = b
    return (i+x,j+y,k+z)


def vector_minus(a,b):
    i,j,k = a
    x,y,z = b
    return (i-x,j-y,k-z)

# ------------------------------------------------------
# Classes

class Cluster(object):
    def __init__(self, root):
        self.beacons = set(root.beacons)
        self.root = root

    def __gt__(self, other):
        return len(self.beacons) > len(other.beacons)

    def __len__(self):
        return len(self.beacons)

    def __iter__(self):
        return iter(self.beacons)

    def __repr__(self):
        return f'{len(self.beacons)}'

    def __str__(self):
        return f'{len(self.beacons)}'

    def find_cluster(self, clusters):
        for i, cluster in enumerate(sorted(clusters)):
            print('\t', i, len(cluster))
            orient, offset = match_orientation(cluster.beacons, self.beacons)
            if orient is not None:
                cluster.merge_cluster(self, orient, offset)
                return

        if not found:
            print('damn it')

    def merge_cluster(self, other, orient, offset):
        aligned = other.orient(orient, offset)
        self.root.add_child(other.root)
        self.beacons = self.beacons.union(aligned)

    def merge_scanner(self, scanner, orient, offset):
        aligned = scanner.orient(orient, offset)
        self.root.add_child(scanner)
        self.beacons = self.beacons.union(aligned)

    def orient(self, idx, offset):
        self.root.orientation = idx
        self.root.offset = offset
        return orient_vectors(self.beacons, idx, offset)



class Scanner(object):
    def __init__(self, name):
        self.name = name
        self.beacons = set()
        self.orientation = 0
        self.offset = (0,0,0)
        self.children = []

    def __str__(self):
        s = f'{self.name}'
        for b in self.beacons:
            s += f'\n{b}'
        return s

    def add(self, line):
        x, y, z = line.strip().split(',')
        vnew = (int(x), int(y), int(z))
        self.beacons.add(vnew)

    def add_child(self, child):
        self.children.append(child)

    def find_cluster(self, clusters):
        for cluster in clusters:
            orient, offset = match_orientation(cluster.beacons, self.beacons)
            if orient is not None:
                cluster.merge_scanner(self, orient, offset)
                return

        print(self.name, 'did not match')
        heapq.heappush(clusters, Cluster(self))


    def orient(self, idx, offset):
        self.orientation = idx
        self.offset = offset
        return orient_vectors(self.beacons, idx, offset)


# ------------------------------------------------------
# Load

def load():
    scanners = []
    current = None

    with io.open(INPUT,'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if line.startswith('---'):
                current = Scanner(line.strip().strip('- '))
                scanners.append(current)
            elif len(line) > 2:
                current.add(line)

    return scanners


# ------------------------------------------------------
# Main



def so_close(scanners):
    beacons = scanners[0].beacons.copy()
    scanner0 = scanners.pop(0)

    while len(scanners):
        scanner = scanners.pop(0)
        print(scanner.name, len(beacons))
        orient, offset = match_orientation(beacons, scanner.beacons)
        if orient is not None:
            aligned = scanner.orient(orient, offset)
            beacons = beacons.union(aligned)
        else:
            print(scanner.name, 'did not match')
            scanners.append(scanner)

    for b in sorted(beacons):
        print(b)
    print(len(beacons))


def main():
    scanners = load()

    clusters = []
    for scanner in scanners:
        print(scanner.name, clusters)
        scanner.find_cluster(clusters)

    while len(clusters) > 1:
        current = heapq.heappop(clusters)
        print(len(current))
        current.find_cluster(clusters)

    for b in sorted(clusters[0]):
        print(b)
    print(len(clusters[0])) # 472


if __name__ == '__main__':
    main()
