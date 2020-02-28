from typing import List

class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    """Stack with left and right wall, stack left, moving right.
      Key: look for the pattern:
             /-\
            /  |
       /---/   -
      /        |
      k    i   j
      At i, start the build up, from left to right, when keep up, keep build, until,
      At j, the wall become shorter, so the expansion of rectangle need to adjust according to j, partial settlement.
      Partial settlement at j: for i, the rectangle span is (j - k) of heights[i], where k is the last index such that
       height[k] < heights[i], e.g., the previous index within stack before i.
    """
    # init stack with (-1, 0): index -1 as the invisible left wall with height 0
    i, n, amax, stack = 0, len(heights), 0, [(-1, 0), ]
    while i < n:
      if heights[i] >= stack[-1][1]:
        stack.append((i, heights[i]))
      else:
        # view this i as the partial right wall
        # all i' from left that higher than i, if form a rectangle with i' height, can't extend beyong i
        while len(stack) > 1 and stack[-1][1] > heights[i]:
          l, lh = stack.pop()
          amax = max(amax, (i - stack[-1][0] - 1) * lh)
        stack.append((i, heights[i]))
      i += 1
    # reach to the rightmost, e.g., global right wall (invisible right wall with heigh 0)
    while len(stack) > 1:
      l, lh = stack.pop()
      amax = max(amax, (n - stack[-1][0] - 1) * lh)
    return amax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0],
    [1],
    [2,1,2],
    [2,1,5,6,2,3],
    [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3],
  ]
  rslts = [solver.largestRectangleArea(heights) for heights in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")