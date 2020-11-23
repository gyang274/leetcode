from typing import List

import itertools

class Solution:
  def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
    # TC: O(N^2), SC: O(N^2)
    # rank: rank[i][j] holds how highly friend i views j, so O(1) comparison on preference.
    rank = [[-1] * n for _ in range(n)]
    for i in range(n):
      for r, j in enumerate(preferences[i]):
        rank[i][j] = r
    # hppy: is unhappy or not
    hppy = [False] * n
    for (x, y), (u, v) in itertools.combinations(pairs, 2):
      if all(hppy[i] for i in (x, y, u, v)):
        continue
      # x, u
      if rank[x][u] < rank[x][y] and rank[u][x] < rank[u][v]:
        hppy[x] = hppy[u] = True
      # x, v
      if rank[x][v] < rank[x][y] and rank[v][x] < rank[v][u]:
        hppy[x] = hppy[v] = True
      # y, u
      if rank[y][u] < rank[y][x] and rank[u][y] < rank[u][v]:
        hppy[y] = hppy[u] = True
      # y, v
      if rank[y][v] < rank[y][x] and rank[v][y] < rank[v][u]:
        hppy[y] = hppy[v] = True
    return sum(hppy)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, [[1], [0]], [[1, 0]]),
    (4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]]),
    (4, [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], [[1, 3], [0, 2]]),
  ]
  rslts = [solver.unhappyFriends(n, preferences, pairs) for n, preferences, pairs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
