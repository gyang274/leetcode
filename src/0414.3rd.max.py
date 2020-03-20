from typing import List

import heapq

class Solution:
  def thirdMax(self, nums: List[int]) -> int:
    nums = set(nums)
    if len(nums) < 3:
      return max(nums)
    pq = []
    for x in nums:
      heapq.heappush(pq, -x)
    # 1st
    heapq.heappop(pq)
    # 2nd
    heapq.heappop(pq)
    # 3rd
    return -heapq.heappop(pq)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1],
    [1, 1],
    [1, 1, 2],
    [1, 1, 2, 3],
    [1, 1, 2, 3, 5],
    [1, 1, 2, 3, 5, 8],
  ]
  rslts = [solver.thirdMax(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")