from typing import List
from collections import defaultdict

class Solution:
  def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
    # build a graph with sentinel source and target nodes
    # source: poor and loudest, target: rich and quietest
    # max length path (s, i) -> richer and quieter candidates
    # s = (n, n), t = (-1, -1)
    n = len(quiet)
    # r: richer
    graph = defaultdict(set)
    for u, v in richer:
      graph[v].add(u)
    # ans as memorization
    ans = [-1] * n
    def dfs(i):
      if ans[i] == -1:
        # init if no child
        ans[i] = i
        # post-order traversal
        for j in graph[i]:
          k = dfs(j)
          if quiet[k] < quiet[ans[i]]:
            ans[i] = k
      return ans[i]
    return list(map(dfs, range(n)))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[0,1],[1,2]], [0,1,2]),
    ([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0]),
  ]
  rslts = [solver.loudAndRich(richer, quiet) for richer, quiet in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
