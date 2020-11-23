from typing import List
from collections import defaultdict, deque

class Solution:
  def minSubarray(self, nums: List[int], p: int) -> int:
    # TC: O(N), SC: O(1).
    n = len(nums)
    # prefix: prefix-sum % p residuals -> index
    prefix, s = defaultdict(deque), 0
    for i, x in enumerate(nums):
      s += x
      s %= p
      prefix[s].append(i)
    # suffix: suffix-sum % p residuals -> index
    suffix, s = defaultdict(deque), 0
    for i, x in reversed(list(enumerate(nums))):
      s += x
      s %= p
      suffix[s].appendleft(i)
    # TC: O(N) in total, amortized O(1) each index in prefix and suffix..
    m = max((prefix[0][-1] + 1) if prefix[0] else 0, (n - suffix[0][0]) if suffix[0] else 0)
    # merge prefix[s] and suffix[r], refr Q1574.
    for s in prefix:
      r = 0 if s == 0 else (p - s)
      i, np = 0, len(prefix[s])
      j, ns = 0, len(suffix[r])
      while i < np and j < ns:
        while j < ns and suffix[r][j] <= prefix[s][i]:
          j += 1
        if j < ns:
          m = max(m, prefix[s][i] + 1 + n - suffix[r][j])
        i += 1
    return -1 if m == 0 else n - m

class Solution:
  def minSubarray(self, nums: List[int], p: int) -> int:
    # TC: O(N), SC: O(1).
    n = len(nums)
    # r: array-sum % p residual 
    r = sum(nums) % p
    if r == 0:
      return 0
    # seen: prefix-sum % p residuals -> last index before current index
    seen, s, m = {0: -1}, 0, n
    for i, x in enumerate(nums):
      s += x
      s %= p
      if (s - r) % p in seen:
        m = min(m, i - seen[(s - r) % p])
      seen[s] = i
    return m if m < n else -1
    

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3], 3),
    ([1,2,3], 7),
    ([3,1,4,2], 6),
    ([6,3,5,2], 9),
  ]
  rslts = [solver.minSubarray(nums, p) for nums, p in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
