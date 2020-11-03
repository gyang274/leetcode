from typing import List
from functools import lru_cache

class Solution:
  @lru_cache(None)
  def recursive(self, i):
    ans = self.x[i]
    for j in range(1, min(self.k + 1, self.n - i)):
      ans = max(ans, self.x[i] + self.recursive(i + j))
    return ans
  def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    self.n, self.x, self.k = len(nums), nums, k
    self.recursive.cache_clear()
    return max(self.recursive(i) for i in range(self.n))

class Solution:
  def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    n = len(nums)
    # dp: walk backward
    ans = nums.copy()
    for i in range(n - 1, -1, -1):
      ans[i] += max([0] + ans[(i + 1):(i + min(k + 1, n - i))])
    return max(ans)

import heapq

class Solution:
  def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    n = len(nums)
    # dp: walk backward, optimized dp process
    ans = nums.copy()
    q = []
    for i in range(n - 1, -1, -1):
      # armortized O(logN)
      while q and q[0][1] - i > k:
        heapq.heappop(q)
      if q:
        ans[i] += max(0, -q[0][0])
      heapq.heappush(q, (-ans[i], i))
    return max(ans)

from collections import deque

class Solution:
  def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    n = len(nums)
    # dp: walk backward, optimized dp process
    ans = nums.copy()
    q = deque([])
    for i in range(n - 1, -1, -1):
      # armortized O(1)
      while q and q[0][1] - i > k:
        q.popleft()
      if q:
        ans[i] += q[0][0]
      while q and ans[i] >= q[-1][0]:
        q.pop()
      if ans[i] >= 0:
        q.append((ans[i], i))
    return max(ans)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([-1,-2,-3], 1),
    ([10,2,-10,5,20], 2),
    ([10,-2,-10,-5,20], 2),
  ]
  rslts = [solver.constrainedSubsetSum(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
