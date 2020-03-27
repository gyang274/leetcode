from typing import List

import heapq

class Solution:
  def minMoves(self, nums: List[int]) -> int:
    # if not nums:
    #   return 0
    q = []
    for x in nums:
      heapq.heappush(q, -x)
    x, i, count = max(nums), 0, 0
    while q:
      y = -heapq.heappop(q)
      count += (x - y) * i
      x = y
      i += 1
    return count

class Solution:
  def minMoves(self, nums: List[int]) -> int:
    nums.sort(reverse=True)
    count = 0
    for i in range(1, len(nums)):
      count += (nums[i - 1] - nums[i]) * i
    return count

class Solution:
  def minMoves(self, nums: List[int]) -> int:
    return sum(nums) - min(nums) * len(nums)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    # [],
    [1],
    [1,1],
    [2,3],
    [2,3,5],
    [2,3,5,8],
    [2,3,5,8,13],
  ]
  rslts = [solver.minMoves(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")