from typing import List


class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    """Stack with left and right wall, stack left, moving right.
    """

    return 0


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    # [0],
    # [1],
    # [2,1,5,6,2,3],
    [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
  ]
  rslts = [solver.largestRectangleArea(heights) for heights in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")