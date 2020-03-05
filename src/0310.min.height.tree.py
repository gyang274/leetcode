from typing import List
from collections import defaultdict

class Solution:
  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    # processing edges
    e = defaultdict(set)
    for x, y in edges:
      e[x].add(y)
      e[y].add(x)
    # all nodes with one and only one edge are leaf node with height 0
    boundary = set([])
    for x in range(n):
      if len(e[x]) <= 1:
        boundary.add(x)
    # level of other nodes are determined by the longest path to the leaf nodes
    extended = set([])
    while boundary:
      if boundary == e.keys():
        return boundary
      while boundary:
        x = boundary.pop()
        for y in e.pop(x):
          e[y].remove(x)
          # key y is in next level only if no other path, so this is the longest path
          if len(e[y]) == 1:
            extended.add(y)
      boundary, extended = extended, set([])
    # n = 1, edges = [], only case no edges.. (or in boundary, for loop over range(n), if len(e[x]) <= 1, ..)
    # return [0]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, []),
    (4, [[1,0],[1,2],[1,3]]),
    (6, [[0,3],[1,3],[2,3],[4,3],[5,4]]),
    (7, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]),
  ]
  rslts = [solver.findMinHeightTrees(n, edges) for n, edges in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")