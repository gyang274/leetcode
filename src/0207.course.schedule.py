from typing import List
from collections import defaultdict

class Solution:
  def dfs(self, visited, boundary):
    while boundary:
      x = boundary.pop()
      if x in visited:
        return False
      visited.add(x)
      if x in self.prep:
        yset = self.prep.pop(x)
        for y in yset:
          if not self.dfs(visited, [y]):
            return False
      visited.remove(x)
    return True
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    """graph, directed, can finish if acyclic, e.g., no cycle.
    """
    self.prep = defaultdict(set)
    for x, y in prerequisites:
      self.prep[x].add(y)
    while self.prep:
      x, y = self.prep.popitem()
      visited, boundary = set([x]), y
      if not self.dfs(visited, boundary):
        return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, [[1,0]]),
    (2, [[1,0],[0,1]]),
    (3, [[0,1],[0,2],[1,2]]),
    (3, [[1,0],[1,2],[0,1]]),
    (4, [[0,1],[1,2],[2,0]]),
  ]
  rslts = [solver.canFinish(numCourses, prerequisites) for numCourses, prerequisites in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")