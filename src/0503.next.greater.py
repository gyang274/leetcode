from typing import List

class Solution:
  def nextGreaterElements(self, nums: List[int]) -> List[int]:
    stack = []
    great = {}
    imax, xmax = -1, float("-inf")
    for i, x in enumerate(nums):
      while stack and x > stack[-1][1]:
        great[stack.pop()] = x
      stack.append((i, x))
      if x > xmax:
        imax, xmax = i, x
    for i in range(imax + 1):
      x = nums[i]
      while stack and x > stack[-1][1]:
        great[stack.pop()] = x
      if not stack:
        break
    return [great.get((i, x), -1) for i, x in enumerate(nums)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1],
    [1,2],
    [2,1],
    [1,2,1],
    [1,2,3,4,5],
    [5,4,3,2,1],
    [100,1,11,1,120,111,123,1,-1,-100],
  ]
  rslts = [solver.nextGreaterElements(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  