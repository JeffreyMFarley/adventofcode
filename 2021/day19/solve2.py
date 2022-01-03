import io

from itertools import combinations
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

def distance_manhattan(a, b):
    s = 0
    for x, y in zip(a, b):
        s += fabs(x - y)
    return s

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
        return f'{self.root.name}: {len(self.beacons)}'

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

    def calculate_offset(self, parent_orient, parent_offset, results):
        results.append((
            self,
            orient_vectors([self.offset], parent_orient, parent_offset).pop()
        ))
        for child in self.children:
            child.calculate_offset(self.orientation, self.offset, results)

    def find_cluster(self, clusters):
        for cluster in clusters:
            orient, offset = match_orientation(cluster.beacons, self.beacons)
            if orient is not None:
                cluster.merge_scanner(self, orient, offset)
                return

        print(self.name, 'did not match')
        clusters.append(Cluster(self))

    def orient(self, idx, offset):
        self.orientation = idx
        self.offset = offset
        return orient_vectors(self.beacons, idx, offset)

    def bfs(self, queue, key=''):
        newkey = f'{key}.{self.name}'
        queue.append((self, newkey))
        for child in self.children:
            child.bfs(queue, newkey)

    def dfs(self, queue):
        for child in self.children:
            child.dfs(queue)
        queue.append(self)

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


def clusterz(scanners):
    clusters = []
    for scanner in scanners:
        scanner.find_cluster(clusters)
        print(scanner.name, clusters)

    while len(clusters) > 1:
        current = clusters.pop(-1)
        print(len(current))
        current.find_cluster(clusters)

    relative = []
    clusters[0].root.bfs(relative)
    for scanner, depth in relative:
        print(depth, scanner.orientation)

    relative = []
    clusters[0].root.calculate_offset(0, (0,0,0), relative)
    for scanner, offset in relative:
        print(scanner.name, scanner.orientation, offset)

    max_dist = 0
    for a,b in combinations(relative, 2):
        scanner0, offset0 = a
        scanner1, offset1 = b
        max_dist = max(distance_manhattan(offset0, offset1), max_dist)

    print(max_dist) # 12092


def main():
    scanners = load()

    known = [(0, scanners[0].beacons.copy())]
    unknown = list(range(1, len(scanners)))

    def search_known(scanner):
        for idx, beacons in reversed(known):
            orient, offset = match_orientation(beacons, scanner.beacons)
            if orient is not None:
                return orient, offset, idx

            orient, offset = match_orientation(
                scanners[idx].beacons, scanner.beacons
            )
            if orient is not None:
                print('non-standard match found')
                o = orient_vectors(
                    [offset],
                    scanners[idx].orientation,
                    scanners[idx].offset
                ).pop()
                return orient, o, idx

        return None, None, None

    while len(unknown):
        current = unknown.pop(0)
        scanner = scanners[current]

        orient, offset, idx = search_known(scanner)
        if orient is not None:
            aligned = scanner.orient(orient, offset)
            print(f'\n{current:02d} matched {idx:02d} at {offset}')
            known.append((current, aligned))
        else:
            print(f'{current},{len(unknown)}\t', end='', flush=True)
            unknown.append(current)

    max_dist = 0
    for s0, s1 in combinations(scanners, 2):
        max_dist = max(distance_manhattan(s0.offset, s1.offset), max_dist)

    print(max_dist) # 12092



if __name__ == '__main__':
    main()
