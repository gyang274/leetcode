from typing import List
from collections import Counter

class Solution:
  def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
    lamps = set(map(tuple, lamps))
    # rows, cols, hill, dial
    rows, cols, hill, dial = Counter(), Counter(), Counter(), Counter()
    for x, y in lamps:
      rows[x] += 1
      cols[y] += 1
      hill[x + y] += 1
      dial[x - y] += 1
    # query
    ans = []
    for u, v in queries:
      ans.append(min(rows[u] + cols[v] + hill[u + v] + dial[u - v], 1))
      for du, dv in [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]:
        x, y = u + du, v + dv
        if 0 <= x < N and 0 <= y < N and (x, y) in lamps:
          rows[x] -= 1
          cols[y] -= 1
          hill[x + y] -= 1
          dial[x - y] -= 1
          lamps.remove((x, y))
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (5, [[0,0],[4,4]], [[1,1],[1,0]]),
  ]
  rslts = [solver.gridIllumination(N, lamps, queries) for N, lamps, queries in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
