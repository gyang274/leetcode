from typing import List

class Solution:
  def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
    # maze compression
    # compress consecutive all blank rows/cols into one row/col
    # len(blocked) <= 200, so len(compressed-maze) <= 604, 604 = 200 * 3 + source + target + 1st + last
    rr, cc = zip(*(blocked + [source, target]))
    rr = set(rr) | {r - 1 for r in rr if r - 1 >= 0} | {r + 1 for r in rr if r + 1 < 10 ** 6}
    cc = set(cc) | {c - 1 for c in cc if c - 1 >= 0} | {c + 1 for c in cc if c + 1 < 10 ** 6}
    # hashmap the index to the compressed maze
    m, n = len(rr), len(cc)
    dr = {x: i for i, x in enumerate(sorted(rr))}
    dc = {x: i for i, x in enumerate(sorted(cc))}
    dd = lambda rc: (dr[rc[0]], dc[rc[1]])
    blocked = set(map(dd, blocked))
    source, target = dd(source), dd(target)
    # bfs/dfs over compressed maze
    queue, seen = [source], set([source])
    for x, y in queue:
      for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        r, c = x + dx, y + dy
        if 0 <= r < m and 0 <= c < n and (r, c) not in seen and (r, c) not in blocked:
          if (r, c) == target:
            return True
          seen.add((r, c))
          queue.append((r, c))
    return False

class Solution:
  def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
    # explore to demonstrate connections
    # since len(blocked) <= 200 => maximum area being blocked <= 19900, by blocking triangle corner
    # so if both source and target can explore an area of > 19900 then must be connected, otherwise
    # contradiction, because if blocked must be blocked within an area <= 19900
    blocked, source, target, m, n = set(map(tuple, blocked)), tuple(source), tuple(target), 10 ** 6, 10 ** 6
    def explore(source, target):
      queue, seen = [source], set([source])
      for x, y in queue:
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
          r, c = x + dx, y + dy
          if 0 <= r < m and 0 <= c < n and (r, c) not in seen and (r, c) not in blocked:
            if (r, c) == target:
              return True
            seen.add((r, c))
            queue.append((r, c))
        if len(queue) > 20000:
          return True
      return False
    return explore(source, target) and explore(target, source)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([], [0,0], [999999,999999]),
    ([[0,1],[1,0]], [0,0], [0,2]),
    ([[0,1],[1,0]], [0,0], [999999,999999]),
  ]
  rslts = [solver.isEscapePossible(blocked, source, target) for blocked, source, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
