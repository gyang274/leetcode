from typing import List

class Solution:
  def minCostToMoveChips(self, position: List[int]) -> int:
    # 2 options, move all to an odd or an even position
    n, m = len(position), sum(x & 1 for x in position)
    return min(m, n - m)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
    [2,2,2,3,3],
  ]
  rslts = [solver.minCostToMoveChips(position) for position in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
