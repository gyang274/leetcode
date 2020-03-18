from typing import List
from functools import lru_cache

class Solution:
  def recursive(self, nums):
    k = tuple(nums)
    print(k)
    if k not in self.memo:
      self.memo[k] = 0
      for i in range(1, len(nums) - 1):
        # recursive doesn't simply the problem enough, need divide and conquer, e.g., half-size problem
        self.memo[k] = max(
          self.memo[k], nums[i - 1] * nums[i] * nums[i + 1] + self.recursive(nums[:i] + nums[(i + 1):])
        )
    return self.memo[k]
  def maxCoins(self, nums: List[int]) -> int:
    """divide and conquer, dynamic programming with memorization.
      dp[(nums)] = max(nums[i - 1] * nums[i] * nums[i + 1], dp[(nums[:i] + nums[(i + 1):])]) 
    """
    self.memo = {}
    return self.recursive([1] + nums + [1])

class Solution:
  def recursive(self, nums, l, r):
    k = (tuple(nums), l, r)
    if k not in self.memo:
      self.memo[k] = 0
      for i in range(len(nums)):
        # divide and conquer, dynamic programming with memorization.
        # an effective divide and conquer to half-size the problems.
        self.memo[k] = max(self.memo[k],
          l * nums[i] * r + self.recursive(nums[:i], l, nums[i]) + self.recursive(nums[(i + 1):], nums[i], r)
        )
    return self.memo[k]
  def maxCoins(self, nums: List[int]) -> int:
    """divide and conquer, dynamic programming with memorization.
      reverse the process of burst balloons as pop up balloon one by one from the final status [1, 1].
    """
    self.memo = {}
    return self.recursive(nums, 1, 1)

class Solution:
  def recursive(self, l, r):
    if (l, r) not in self.memo:
      self.memo[(l, r)] = 0
      for i in range(l + 1, r):
        # divide and conquer, dynamic programming with memorization.
        # an effective divide and conquer to half-size the problems.
        self.memo[(l, r)] = max(self.memo[(l, r)],
          self.nums[l] * self.nums[i] * self.nums[r] + self.recursive(l, i) + self.recursive(i, r)
        )
    return self.memo[(l, r)]
  def maxCoins(self, nums: List[int]) -> int:
    """divide and conquer, dynamic programming with memorization.
      reverse the process of burst balloons as pop up balloon one by one from the final status [1, 1].
    """
    self.memo = {}
    self.nums = [1] + nums + [1]
    return self.recursive(0, len(self.nums) - 1)

class Solution:
  @lru_cache(None)
  def recursive(self, l, r):
    xmax = 0
    for i in range(l + 1, r):
      # divide and conquer, dynamic programming with memorization.
      # an effective divide and conquer to half-size the problems.
      xmax = max(xmax,
        self.nums[l] * self.nums[i] * self.nums[r] + self.recursive(l, i) + self.recursive(i, r)
      )
    return xmax
  def maxCoins(self, nums: List[int]) -> int:
    """divide and conquer, dynamic programming with memorization.
      reverse the process of burst balloons as pop up balloon one by one from the final status [1, 1].
    """
    self.nums = [1] + nums + [1]
    # key: cache_clear() each time run on a set of balloons, e.g., nums.
    self.recursive.cache_clear()
    return self.recursive(0, len(self.nums) - 1)

class Solution:
  def maxCoins(self, nums: List[int]) -> int:
    """divide and conquer, dynamic programming with memorization.
      reverse the process of burst balloons as pop up balloon one by one from the final status [1, 1].
    """
    nums = [1] + nums + [1]
    n = len(nums)
    memo = [[0] *  n for _ in range(n)]
    for l in range(n - 3, -1, -1):
      for r in range(l + 2, n):
        for i in range(l + 1, r):
          memo[l][r] = max(memo[l][r], nums[l] * nums[i] * nums[r] + memo[l][i] + memo[i][r])
    return memo[0][-1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [2],
    [2,5],
    [2,3,5],
    [3,2,5,8],
    [8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2]
  ]
  rslts = [solver.maxCoins(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")