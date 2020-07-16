from typing import List
from collections import defaultdict, Counter
from functools import lru_cache
from math import factorial

class Solution:
  def numSquarefulPerms(self, A: List[int]) -> int:
    """dynamic programming, O(N^2 2^N), num of hamilton path on undirect graph.
    """
    # graph, nodes are connected iff make a square
    n, graph = len(A), defaultdict(set)
    squareOk = lambda x, y: int((x + y) ** 0.5) ** 2 == x + y
    for j in range(n):
      for i in range(j):
        if squareOk(A[i], A[j]):
          graph[i].add(j)
          graph[j].add(i)
    # find num of hamiltonian paths in graph
    @lru_cache(None)
    def dfs(node, visited):
      if visited == (1 << n) - 1:
        return 1
      ans = 0
      for nuxt in graph[node]:
        if visited & (1 << nuxt) == 0:
          ans += dfs(nuxt, visited | (1 << nuxt))
      return ans
    ans = sum(dfs(i, 1 << i) for i in range(n))
    # remove duplicates
    count = Counter(A)
    for v in count.values():
      if v > 1:
        ans //= factorial(v)
    return ans

class Solution:
  def numSquarefulPerms(self, A: List[int]) -> int:
    """backtrack.
    """
    d = Counter(A)
    graph = {i: {j for j in d if int((i + j) ** 0.5) ** 2 == i + j} for i in d}
    # backtrack
    def dfs(x, left=len(A) - 1):
      d[x] -= 1
      count = sum(dfs(y, left - 1) for y in graph[x] if d[y]) if left else 1
      d[x] += 1
      return count
    return sum(map(dfs, d))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,8,8,17,24],
    [2,2,2,2,2,2,2,2,2,2,2],
  ]
  rslts = [solver.numSquarefulPerms(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
