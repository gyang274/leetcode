from typing import List
from collections import defaultdict

class Solution:
  def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
    # courses
    courses = {x + 1 for x in range(N)}
    # prerequisite
    dprev = defaultdict(set)
    dnext = defaultdict(set)
    for x, y in relations:
      dnext[x].add(y)
      dprev[y].add(x)
      courses.discard(y)
    semesters, n = 0, 0
    while courses:
      # take all in one semester
      semesters += 1
      n += len(courses)
      # prep for the next semester
      cnext = set()
      for x in courses:
        for y in dnext[x]:
          dprev[y].remove(x)
          if not dprev[y]:
            cnext.add(y)
      courses = cnext
    return -1 if n < N else semesters

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, [[1,3],[2,3]]),
    (3, [[1,2],[2,3],[3,1]]),
  ]
  rslts = [solver.minimumSemesters(N, relations) for N, relations in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
