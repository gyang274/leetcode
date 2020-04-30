from typing import List

class Solution:
  def findLengthOfLCIS(self, nums: List[int]) -> int:
    prev, count, cmax = float("-inf"), 0, 0
    for x in nums:
      if x > prev:
        count += 1
        cmax = max(cmax, count)
      else:
        count = 1
      prev = x
    return cmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,3,5,4,7],
    [2,2,2,2,2],
  ]
  rslts = [solver.findLengthOfLCIS(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
