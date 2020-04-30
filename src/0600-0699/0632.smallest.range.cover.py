from typing import List
from collections import deque, defaultdict

import heapq

class Solution:
  def smallestRange(self, nums: List[List[int]]) -> List[int]:
    queue = sorted([(val, idx) for idx, num in enumerate(nums) for val in num])
    q, n = len(queue), len(nums)
    xmin, xmax = queue[0][0], queue[-1][0]
    i, j, d = 0, 0, defaultdict(lambda: 0)
    while i < q:
      while j < q and len(d) < n:
        d[queue[j][1]] += 1
        j += 1
      if len(d) == n:
        while d[queue[i][1]] > 1:
          d[queue[i][1]] -= 1
          i += 1
        if queue[j - 1][0] - queue[i][0] < xmax - xmin:
          xmin, xmax = queue[i][0], queue[j - 1][0]
      d[queue[i][1]] -= 1
      if d[queue[i][1]] == 0:
        d.pop(queue[i][1])
      i += 1
    return xmin, xmax

class Solution:
  def smallestRange(self, nums: List[List[int]]) -> List[int]:
    queue = sorted([(num[0], 0, idx) for idx, num in enumerate(nums) if num])
    if len(queue) < len(nums):
      if not len(queue):
        return []
      else:
        return [min([num[0] for num in nums if num]), max([num[-1] for num in nums if num])]
    # priority queue
    heapq.heapify(queue)
    xmin, xmax = queue[0][0], queue[-1][0]
    vmin, vmax = queue[0][0], queue[-1][0]
    while True:
      _, k, i = heapq.heappop(queue)
      if k + 1 == len(nums[i]):
        break
      v = nums[i][k + 1]
      heapq.heappush(queue, (v, k + 1, i))
      vmin = queue[0][0]
      vmax = max(vmax, v)
      if vmax - vmin < xmax - xmin:
        xmin, xmax = vmin, vmax
    return xmin, xmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]],
    [[4,10,15,24,26], [0,9,12,20], [5,18,22,30],[]],
  ]
  rslts = [solver.smallestRange(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
