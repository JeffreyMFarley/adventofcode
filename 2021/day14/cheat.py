    def bfs(start, goal, twice):
        queue = [(start,set(),twice)]
        while queue:
            current,small,twice = queue.pop(0)
            if current == goal:
                yield 1
            elif current.islower():
                twice &= current not in small
                small.add(current)
            for node in maze.get(current,[]):
                if node not in small or twice:
                    queue.append((node,small.copy(),twice))

    maze = {}
    for line in open(INPUT).read().splitlines():
        s,e = line.split('-')
        if s!='end' and e!='start': maze.setdefault(s,set()).add(e)
        if e!='end' and s!='start': maze.setdefault(e,set()).add(s)

    print('part1',sum(bfs('start', 'end', 0)))
    print('part2',sum(bfs('start', 'end', 1)))
