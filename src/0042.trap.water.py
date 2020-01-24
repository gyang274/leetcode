from typing import List


class Solution:
  def trap(self, height: List[int]) -> int:
    """
    Maintain 2 list of partial potential views, 
      one scan from left to right, represent potential from lft view, 
      one scan from right to left, represent potential from rgt view, 
    Then, take the min at each position, O(3n).
    """
    l = [0 for _ in height]
    r = [0 for _ in height]
    lhmax = -1
    for i, h in enumerate(height):
      lhmax = max(lhmax, h)
      l[i] = lhmax - h
    rhmax = -1
    for i, h in reversed(list(enumerate(height))):
      rhmax = max(rhmax, h)
      r[i] = rhmax - h
    return sum([min(lh, rh) for lh, rh in zip(l, r)])


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [0,1,0,2,1,0,1,3,2,1,2,1],
  ]
  rslts = [solver.trap(height) for height in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")