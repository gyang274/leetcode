from typing import List

class Solution:
  def findCircleNum(self, M: List[List[int]]) -> int:
    n = len(M)
    students, circle = set([i for i in range(n)]), 0
    while students:
      circle += 1
      interior, exterior = set([students.pop()]), set([])
      while interior:
        for i in interior:
          frontier = set([])
          for s in students:
            if M[i][s] == 1:
              frontier.add(s)
          students -= frontier
          exterior |= frontier
        interior, exterior = exterior, set([])
    return circle

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      [1,1,0],
      [1,1,0],
      [0,0,1]
    ],
    [
      [1,1,0],
      [1,1,1],
      [0,1,1]
    ],
  ]
  rslts = [solver.findCircleNum(M) for M in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
