from typing import List

class Solution:
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    """Q0435, greedy approach.
    """
    if not points:
      return 0
    # sort w.r.t start, ended
    points.sort()
    # covered start and ended, greedy approach
    cs, ce, count = float("-inf"), float("-inf"), 0
    for s, e in points:
      if s > ce:
        cs, ce = s, e
        count += 1
      else:
        ce = min(e, ce)
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [[0,1]],
    [[0,1],[1,2]],
    [[0,1],[0,1],[0,1]],
    [[0,1],[0,2],[1,2],[1,3],[2,3],[3,4]],
  ]
  rslts = [solver.findMinArrowShots(points) for points in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")