from typing import List
from collections import defaultdict

class Solution:
  def recursive(self, v, d):
    for k in d:
      v += d[k]
      self.xmax = max(self.xmax, v)
      dk = d.copy()
      dk.pop(k)
      if k - 1 in dk:
        dk.pop(k - 1)
      if k + 1 in dk:
        dk.pop(k + 1)
      if dk:
        self.recursive(v, dk)
      v -= d[k]
    return None
  def deleteAndEarn(self, nums: List[int]) -> int:
    d = defaultdict(lambda: 0)
    for x in nums:
      d[x] += x
    self.xmax = 0
    self.recursive(0, d)    
    return self.xmax

class Solution:
  def deleteAndEarn(self, nums: List[int]) -> int:
    """sort O(N + KlogK) + dynamic programming (one pass) O(K), N is length of nums, K is unqiue values in nums
    """
    if not nums:
      return 0
    # sort (key, value)
    d = defaultdict(lambda: 0)
    for x in nums:
      d[x] += x
    n, xs = len(d), sorted([(k, d[k]) for k in d])
    # dynamic programming
    dp = [0] * (n + 1)
    dp[-2] = xs[-1][1]
    for i in range(n - 2, -1, -1):
      if xs[i][0] == xs[i + 1][0] - 1:
        dp[i] = max(xs[i][1] + dp[i + 2], dp[i + 1])
      else:
        dp[i] = xs[i][1] + dp[i + 1]
    return dp[0]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [2,2,3,3,3,4],
  ]
  rslts = [solver.deleteAndEarn(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
