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
  def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
    # Q0207, Q0210, topological sort at group level then item level, O(V + E)
    # group level topological sort (each -1 as a separate group)
    # d: group -> items
    d = defaultdict(list)
    for i in range(n):
      if group[i] == -1:
        group[i] = m
        m += 1
      d[group[i]].append(i)
    prerequisites = set()
    for i, js in enumerate(beforeItems):
      for j in js:
        if not group[i] == group[j]:
          prerequisites.add((group[i], group[j]))
    schedule = self.topologicalSort([x for x in range(m)], prerequisites)
    # items level topological sort within each group
    ans = []
    if schedule:
      for g in schedule:
        items = d[g]
        iprep = []
        for i in items:
          for j in beforeItems[i]:
            if group[i] == group[j]:
              iprep.append((i, j))
        if iprep:
          ischedule = self.topologicalSort(items, iprep)
          if ischedule:
            ans.extend(ischedule)
          else:
            return []
        else:
          ans.extend(items)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (5, 3, [0,0,2,1,0], [[3],[],[],[],[1,3,2]]),
    (8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3,6],[],[],[]]),
    (8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3,6],[],[4],[]]),
  ]
  rslts = [solver.sortItems(n, m, group, beforeItems) for n, m, group, beforeItems in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
