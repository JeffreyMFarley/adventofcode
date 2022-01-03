import io

from collections import defaultdict, Counter

INPUT = 'input1.txt'

START = 'start'
END = 'end'

# ------------------------------------------------------
# Classes

class Node(object):
    def __init__(self, name):
        self.name = name
        self.isBig = name.isupper()
        self.isSmol = name.islower() and name != START and name != END

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name


# class Edge(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __eq__(self, other):
#         return str(self) == str(other)
#
#     def __hash__(self):
#         return hash(str(self))
#
#     def __str__(self):
#         return '{} -> {}'.format(self.start, self.end)


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)

    def __str__(self):
        s = ''
        for n in self.nodes:
            s += f'\033[1m{n}\033[0m\n' if n.isBig else f'{n}\n'
            for e in self.edges[n]:
                s += f'\t{e}\n'

        return s

    def add(self, a, b):
        A = Node(a)
        self.nodes.add(A)
        B = Node(b)
        self.nodes.add(B)
        self.edges[A].append(B)
        self.edges[B].append(A)

    def traverals(self):
        paths = set()

        dfs = self.edges.copy()

        queue = []
        start = Node('start')

        edges = dfs.pop(start)
        for e in edges:
            queue.append(Path([start, e]))

        while len(queue):
            curr = queue.pop(0)
            #print(len(queue), curr)
            node = curr.end
            edges = dfs[node]
            for e in edges:
                p = curr.copy()
                #print(f'\t{node} -> {e}\t{p}')
                if str(e) == END:
                    p.add(e)
                    paths.add(p)
                elif not p.seen(e):
                    p.add(e)
                    queue.append(p)

        return paths


class Path(object):
    def __init__(self, steps=[], visited=None, smol=None):
        if visited is None:
            self.steps = []
            self.visited = set()
            self.smol = Counter()
            for st in steps:
                self.add(st)
        else:
            self.steps = list(steps)
            self.visited = visited.copy()
            self.smol = smol.copy()

    def __lt__(self, other):
        return str(self) < str(other)

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        steps = ','.join([str(x) for x in self.steps])
        smol = ','.join([f'{k}: {v}' for k, v in self.smol.items()])
        return f'{steps}\t{smol}'

    def add(self, node):
        self.steps.append(node)
        if str(node) == START:
            self.visited.add(node)
        elif node.isSmol:
            max_smol = max(list(self.smol.values()) + [0])
            if self.smol[node] < 1 and max_smol < 1:
                self.smol[node] += 1
            else:
                self.visited.add(node)

    def copy(self):
        clone = Path(self.steps, self.visited, self.smol)
        return clone

    def seen(self, node):
        return node in self.visited

    @property
    def end(self):
        return self.steps[-1]

# ------------------------------------------------------
# Load

def load():
    graph = Graph()
    with io.open(INPUT,'r', encoding='utf-8') as f:
        for line in f:
            a, b = line.strip().split('-')
            graph.add(a, b)

    return graph

# ------------------------------------------------------
#


# ------------------------------------------------------
# Main

def main():
    graph = load()
    print(graph)

    paths = graph.traverals()
    print('\n'.join([str(x) for x in sorted(paths)]))
    print(len(paths))


if __name__ == '__main__':
    main()
