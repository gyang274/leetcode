class Solution:
  def minKnightMoves(self, x: int, y: int) -> int:
    q, seen = [(x, y, 0)], set()
    for x, y, m in q:
      if x == y == 0:
        return m
      if (x, y) not in seen:
        seen.add((x, y))
        q.append((x - 2, y - 1, m + 1))
        q.append((x - 2, y + 1, m + 1))
        q.append((x + 2, y - 1, m + 1))
        q.append((x + 2, y + 1, m + 1))
        q.append((x - 1, y - 2, m + 1))
        q.append((x - 1, y + 2, m + 1))
        q.append((x + 1, y - 2, m + 1))
        q.append((x + 1, y + 2, m + 1))
    return -1

import heapq

class Solution:
  def minKnightMoves(self, x: int, y: int) -> int:
    # a-star search with heuristic h(x, y) = (abs(x) + abs(y) - 1) // 3 + 1
    q, seen = [((abs(x) + abs(y) - 1) // 3 + 1, 0, x, y)], {}
    while q:
      e, d, x, y = heapq.heappop(q)
      if x == y == 0:
        return d
      if (x, y) not in seen or seen[(x, y)] > d:
        seen[(x, y)] = d
        for dx, dy in [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]:
          heapq.heappush(q, ((abs(x + dx) + abs(y + dy) - 1) // 3 + 1 + d + 1, d + 1, x + dx, y + dy))
    return -1

class Solution:
  def minKnightMoves(self, x: int, y: int) -> int:
    # O(1)
    # symmetric of axis
    x, y = abs(x), abs(y)
    # symmetric of diagonal
    x, y = min(x, y), max(x, y)
    # init
    if (x, y) == (0, 1):
      return 3
    if (x, y) == (2, 2):
      return 4
    d = y - x
    if x > d:
      return d - 2 * ((d - x) // 3)
    else:
      return d - 2 * ((d - x) // 4)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 3),
    (5, 5),
    (100, 200),
  ]
  rslts = [solver.minKnightMoves(x, y) for x, y in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
