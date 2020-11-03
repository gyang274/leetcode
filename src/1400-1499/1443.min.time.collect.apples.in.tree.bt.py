from typing import List
from collections import defaultdict

class Solution:
  def recursive(self, u):
    x = 0
    for v in self.tree[u]:
      x += self.recursive(v)
    if x > 0 or self.apple[u]:
      x += 2
    return x
  def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    self.apple = hasApple
    # contruct tree with root 0
    graph = defaultdict(set)
    for u, v in edges:
      graph[u].add(v)
      graph[v].add(u)
    self.tree, queue, seen = defaultdict(set), [0], {0}
    while queue:
      qnext = []
      for u in queue:
        for v in graph[u]:
          if v not in seen:
            self.tree[u].add(v)
            qnext.append(v)
            seen.add(v)
      queue = qnext
    # Key: an edge is used iff its subtree hasApple.
    #  if an edge is used, it used twice, and twice only - going down and back up.
    return max(0, self.recursive(0) - 2)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (4, [[0,2],[0,3],[1,2]], [False,True,False,False]),
    (7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]),
    (7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False]),
    (7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,False,False,False,False,False]),
  ]
  rslts = [solver.minTime(n, edges, hasApple) for n, edges, hasApple in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
