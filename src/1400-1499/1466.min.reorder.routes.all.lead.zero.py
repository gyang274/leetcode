from typing import List
from collections import defaultdict

class Solution:
  def minReorder(self, n: int, connections: List[List[int]]) -> int:
    # forward and backward of current routes
    f, b = defaultdict(set), defaultdict(set)
    for u, v in connections:
      f[u].add(v)
      b[v].add(u)
    # bfs on backwards, reverse when blocked
    q, seen, count = {0}, {0}, 0
    while q:
      nuxt = set()
      for v in q:
        for u in b[v]:
          if u not in seen:
            nuxt.add(u)
            seen.add(u)
      if not nuxt:
        for u in seen:
          for v in f[u]:
            if v not in seen and v not in nuxt:
              nuxt.add(v)
              count += 1
        seen = seen.union(nuxt)
      q = nuxt
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, [[1,0],[2,0]]),
    (5, [[1,0],[1,2],[3,2],[3,4]]),
    (6, [[0,1],[1,3],[2,3],[4,0],[4,5]]),
  ]
  rslts = [solver.minReorder(n, connections) for n, connections in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
