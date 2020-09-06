from typing import List

class Solution:
  def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    p = coordinates
    s = False if p[1][0] == p[0][0] else True
    for i in range(2, len(p)):
      if not s:
        if not p[i][0] == p[0][0]:
          return False
      else:
        # use multiplication to avoid numeric issue.
        # if (p[i][1] - p[0][1]) / (p[i][0] - p[0][0]) == (p[1][1] - p[0][1]) / (p[1][0] - p[0][0]):
        if not (p[i][1] - p[0][1]) * (p[1][0] - p[0][0]) == (p[1][1] - p[0][1]) * (p[i][0] - p[0][0]):
          return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]],
    [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]],
  ]
  rslts = [solver.checkStraightLine(coordinates) for coordinates in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
