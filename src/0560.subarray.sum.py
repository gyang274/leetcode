from typing import List
from collections import defaultdict

class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    d = defaultdict(lambda: 0)
    s, count = 0, 0
    for x in nums:
      s += x
      if s == k:
        count += 1
      if s - k in d:
        count += d[s - k]
      d[s] += 1
    return count

class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    d = defaultdict(lambda: 0)
    s, count, d[0] = 0, 0, 1
    for x in nums:
      s += x
      if s - k in d:
        count += d[s - k]
      d[s] += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,1,1], 2),
    ([1,0,-1], 0),
    ([2,3,1,1,4], 5),
    ([3,2,1,0,4], 5),
    ([1,0,-1,1,0,-1,0,0,1,-1,1,1,-1,-1], 0),
  ]
  rslts = [solver.subarraySum(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
