from typing import List
from collections import defaultdict

class Solution:
  def validTree(self, n: int, edges: List[List[int]]) -> bool:
    """Tree: undirect, connected and acyclic graph. Q0207, Q0210.
    """
    if not n - 1 == len(edges):
      return False
    edict = defaultdict(set)
    for e in edges:
      edict[e[0]].add(e[1])
      edict[e[1]].add(e[0])
    visited, boundary = set([]), set([0])
    while boundary:
      node = boundary.pop()
      visited.add(node)
      if node in edict:
        unvisited = edict.pop(node)
        for nuxt in unvisited:
          edict[nuxt].remove(node)
          if nuxt in visited or nuxt in boundary or nuxt == node:
            return False
          boundary.add(nuxt)
    if edict:
      return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (0, []),
    (1, []),
    (2, []),
    (2, [[0,1]]),
    (3, [[2,0],[2,1]]),
    (5, [[0,1], [0,2], [0,3], [1,4]]),
    (5, [[0,1], [1,2], [2,3], [1,3], [1,4]]),
  ]
  rslts = [solver.validTree(n, edges) for n, edges in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")