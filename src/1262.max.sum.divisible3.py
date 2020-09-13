from typing import List

import heapq

class Solution:
  def maxSumDivThree(self, nums: List[int]) -> int:
    s = sum(nums)
    r = s % 3
    if r == 0:
      return s
    heapq.heapify(nums)
    while nums:
      x = heapq.heappop(nums)
      while x % 3 == 0 and nums:
        x = heapq.heappop(nums)
      if x % 3 == r:
        return s - x
      if nums:
        y = heapq.heappop(nums)
        while y % 3 == 0 and nums:
          y = heapq.heappop(nums)
        if y % 3 == r:
          return s - y
        if (x % 3) * (y % 3) != 0:
          heapq.heappush(nums, x + y)
    return 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
    [3,4,5,6,7],
  ]
  rslts = [solver.maxSumDivThree(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
