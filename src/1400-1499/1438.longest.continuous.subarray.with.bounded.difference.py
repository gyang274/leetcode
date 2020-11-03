from typing import List

import heapq

class Solution:
  def longestSubarray(self, nums: List[int], limit: int) -> int:
    # TC: O(NlogN)
    xmin, xmax, xlft, xlen = [], [], -1, 0
    for i, x in enumerate(nums):
      heapq.heappush(xmin, (+x, i))
      heapq.heappush(xmax, (-x, i))
      while -xmax[0][0] - xmin[0][0] > limit:
        if xmax[0][1] < xmin[0][1]:
          _, xlft = heapq.heappop(xmax)
        else:
          _, xlft = heapq.heappop(xmin)
        while xmax[0][1] < xlft:
          heapq.heappop(xmax)
        while xmin[0][1] < xlft:
          heapq.heappop(xmin)
      xlen = max(xlen, i - xlft)
    return xlen

from collections import deque

class Solution:
  def longestSubarray(self, nums: List[int], limit: int) -> int:
    # TC: O(N), use queue, maintain the monotonicity
    # xmax: queue of value decrease while index increase
    # xmin: queue of value increase while index increase
    xmax, xmin, xlft, xlen = deque([]), deque([]), -1, 0
    for i, x in enumerate(nums):
      while xmax and x > xmax[-1][0]:
        xmax.pop()
      xmax.append((x, i))
      while xmin and x < xmin[-1][0]:
        xmin.pop()
      xmin.append((x, i))
      while xmax[0][0] - xmin[0][0] > limit:
        if xmax[0][1] < xmin[0][1]:
          _, xlft = xmax.popleft()
        else:
          _, xlft = xmin.popleft()
      xlen = max(xlen, i - xlft)
    return xlen

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([8,2,4,7], 4),
    ([10,1,2,4,7,2], 5),
    ([4,2,2,2,4,4,2,2], 0),
    ([7,40,10,10,40,39,96,21,54,73,33,17,2,72,5,76,28,73,59,22,100,91,80,66,5,49,26,45,13,27,74,87,56,76,25,64,14,86,50,38,65,64,3,42,79,52,37,3,21,26,42,73,18,44,55,28,35,87], 63),
  ]
  rslts = [solver.longestSubarray(nums, limit) for nums, limit in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
