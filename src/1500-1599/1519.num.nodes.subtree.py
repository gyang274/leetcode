from typing import List
from collections import defaultdict

class Solution:
  def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
    # graph
    graph = defaultdict(set)
    for u, v in edges:
      graph[u].add(v)
      graph[v].add(u)
    # recursive
    ans, seen = [0] * n, {0}
    def dfs(u):
      view = [0] * 26
      for v in graph[u]:
        if v not in seen:
          seen.add(v)
          for i, x in enumerate(dfs(v)):
            view[i] += x
      # add this one view
      x = ord(labels[u]) - ord('a')
      view[x] += 1
      # add this one into ans..
      ans[u] = view[x]
      return view
    dfs(0)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (4, [[0,1],[1,2],[0,3]], "bbbb"),
    (5, [[0,1],[0,2],[1,3],[0,4]], "aabab"),
    (6, [[0,1],[0,2],[1,3],[3,4],[4,5]], "cbabaa"),
    (7, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], "aaabaaa"),
    (7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd"),
  ]
  rslts = [solver.countSubTrees(n, edges, labels) for n, edges, labels in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
