from typing import List

class Solution:
  def longestSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    if all(nums):
      return n - 1
    x0, x1, mx = 0, 0, 0
    for i in range(n):
      if nums[i]:
        x0 += 1
        x1 += 1
        mx = max(mx, x1)
      else:
        x0, x1 = 0, x0
    return mx

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0], [1], [0,1], [1,1], [1,0,1,1], [1,0,1,1,0,1,1,1],
  ]
  rslts = [solver.longestSubarray(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
