import io
import heapq

INPUT = 'input1.txt'

# ------------------------------------------------------
# Classes


# ------------------------------------------------------
# Load

def load():
    with io.open(INPUT,'r', encoding='utf-8') as f:
        grid = {}
        for y, line in enumerate(f):
            for x, w in enumerate(line.strip()):
                grid[(x, y)] = int(w)

    return grid, x, y

# ------------------------------------------------------
#

def dijkstra(grid, target, start=(0, 0), risk=0):
  queue = [(risk, start)]
  minRisk = {start: risk}
  visited = set([start])

  while queue:
    risk, (x, y) = heapq.heappop(queue)
    if (x, y) == target:
        return risk

    for neighb in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
      if neighb not in grid or neighb in visited:
          continue

      visited.add(neighb)
      newRisk = risk + grid[neighb]
      if newRisk < minRisk.get(neighb, 999999):
        minRisk[neighb] = newRisk
        heapq.heappush(queue, (newRisk, neighb))

# ------------------------------------------------------
# Main

def main():
    grid_sm, dim_x, dim_y = load()

    grid = {}

    for j in range(5):
        for i in range(5):
            for (x, y), w in grid_sm.items():
                newXY = (x + (dim_x+1) * i, y + (dim_y+1) * j)
                newW = w + i + j
                grid[newXY] = newW if newW < 10 else newW % 9

    dim_x, dim_y = map(max, zip(*grid))

    # for y in range(dim_y + 1):
    #     s = ''
    #     for x in range(dim_x + 1):
    #         s += str(grid[(x, y)])
    #     print(s)

    print(dijkstra(grid, (dim_x, dim_y)))

if __name__ == '__main__':
    main()
