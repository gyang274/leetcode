from typing import List
from collections import Counter

import heapq

class Solution:
  def findShortestSubArray(self, nums: List[int]) -> int:
    cntr = [(-v, k) for k, v in Counter(nums).items()]
    heapq.heapify(cntr)
    cmax = cntr[0][0]
    if cmax == -1:
      return 1
    n = len(nums)
    span, revs = n, nums[::-1]
    while cntr and cntr[0][0] == cmax:
      v, k = heapq.heappop(cntr)
      span = min(span, n - nums.index(k) - revs.index(k))
    return span

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.findShortestSubArray(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
