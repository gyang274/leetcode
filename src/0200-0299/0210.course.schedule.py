from typing import List
from collections import defaultdict

class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    """graph, directed, growing the `can finish` courses init from courses w.o. prerequisites.
    """
    # construct prerequisites 
    # prep: x ->requires set(y1, y2, ..), before take x need y1, y2, ..
    # post: y ->followup set(x1, x2, ..), 
    #   after take y, it is possible (only possible may not, as x_i might need others) x1, x2, ..
    prep = defaultdict(set)
    post = defaultdict(set)
    for x, y in prerequisites:
      prep[x].add(y)
      post[y].add(x)
    # schedule
    #  start with all courses requires no prerequisites
    schedule, boundary = [], [x for x in range(numCourses) if x not in prep]
    while boundary:
      y = boundary.pop()
      schedule.append(y)
      if y in post:
        xs = post.pop(y)
        for x in xs:
          prep[x].remove(y)
          # all prerequisites of x are cleared 
          if not prep[x]:
            prep.pop(x)
            boundary.append(x)
    # some courses are impossible to complete?
    if prep:
      return []
    return schedule

class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    """graph, directed, growing the `can finish` courses init from courses w.o. prerequisites.
      change the prep to simply count for number of courses needed before taking x, e.g., indegree.
    """
    # construct prerequisites 
    # prep: x ->requires set(y1, y2, ..), before take x need y1, y2, ..
    # post: y ->followup set(x1, x2, ..), 
    #   after take y, it is possible (only possible may not, as x_i might need others) x1, x2, ..
    prep = defaultdict(lambda: 0)
    post = defaultdict(set)
    for x, y in prerequisites:
      prep[x] += 1
      post[y].add(x)
    # schedule
    #  start with all courses requires no prerequisites
    schedule, boundary = [], [x for x in range(numCourses) if x not in prep]
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
    # some courses are impossible to complete?
    if prep:
      return []
    return schedule

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, [[1,0]]),
    (2, [[1,0],[0,1]]),
    (3, [[0,1],[0,2],[1,2]]),
    (3, [[1,0],[1,2],[0,1]]),
    (4, [[0,1],[1,2],[2,0]]),
    (4, [[1,0],[2,0],[3,1],[3,2]]),
  ]
  rslts = [solver.findOrder(numCourses, prerequisites) for numCourses, prerequisites in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")