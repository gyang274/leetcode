from typing import List

class Solution:
  def heightChecker(self, heights: List[int]) -> int:
    return sum(x != y for x, y in zip(heights, sorted(heights)))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,1,4,2,1,3],
  ]
  rslts = [solver.heightChecker(heights) for heights in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
