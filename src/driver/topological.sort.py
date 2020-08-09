from typing import List
from collections import defaultdict

class Solution:
  def topologicalSort(self, nodes: List[int], prerequisites: List[List[int]]) -> List[int]:
    """Topological Sort, O(V + E).
    Args:
      nodes: nodes in graph.
      prerequisites: list of (x, y), where y is a preprequisite of x, e.g., y -> x in directed graph.
    Algo:
      Kahn's algorithm: grow the _no dependency_ nodes init from nodes w.o. prerequisites.
    """
    # graph
    #  prep: x ->requires set(y1, y2, ..), before take x need y1, y2, .., takes count only
    #  post: y ->followup set(x1, x2, ..), 
    #   after take y, it is possible (only possible may not, as x_i might need others) x1, x2, ..
    prep = defaultdict(lambda: 0)
    post = defaultdict(set)
    for x, y in prerequisites:
      prep[x] += 1
      post[y].add(x)
    # schedule
    #  start with all nodes requires no prerequisites
    schedule, boundary = [], [x for x in nodes if x not in prep]
    while boundary:
      y = boundary.pop()
      schedule.append(y)
      if y in post:
        xs = post.pop(y)
        for x in xs:
          prep[x] -= 1
          # all prerequisites of x are cleared 
          if prep[x] == 0:
            prep.pop(x)
            boundary.append(x)
    # some nodes are impossible to complete?
    if prep:
      return []
    return schedule

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([0,1], [[1,0]]),
    ([0,1], [[1,0],[0,1]]),
    ([0,1,2], [[0,1],[0,2],[1,2]]),
    ([0,1,2], [[1,0],[1,2],[0,1]]),
    ([0,1,2,3], [[0,1],[1,2],[2,0]]),
    ([0,1,2,3], [[1,0],[2,0],[3,1],[3,2]]),
  ]
  rslts = [solver.topologicalSort(nodes, prerequisites) for nodes, prerequisites in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")