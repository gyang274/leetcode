from typing import List


class Solution:
  def maxArea(self, height: List[int]) -> int:
    i, j = 0, len(height) - 1
    h = min(height[i], height[j])
    x = (j - i) * h
    while i < j:
      if height[i] <= height[j]:
        # move i
        i += 1
      else:
        # move j
        j -= 1
      if height[i] >= h and height[j] >= h and (j - i) * min(height[i], height[j]) > x:
        h = min(height[i], height[j])
        x = (j - i) * h
    return x


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
    [4, 2],
  ]
  rslts = [solver.maxArea(height) for height in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")