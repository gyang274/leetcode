from typing import List

class Solution:
  def projectionArea(self, grid: List[List[int]]) -> int:
    # projection on xy, xz, yz
    return sum(map(lambda r: sum(map(lambda x: x > 0, r)), grid)) + sum(map(max, grid)) + sum(map(max, zip(*grid)))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[2]],
    [[1,2],[3,4]],
    [[1,0],[0,2]],
    [[1,1,1],[1,0,1],[1,1,1]],
    [[2,2,2],[2,1,2],[2,2,2]],
  ]
  rslts = [solver.projectionArea(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
