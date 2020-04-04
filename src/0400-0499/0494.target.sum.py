from typing import List

class Solution:
  def backtrack(self, x, i):
    # x: sum at the moment, i: index to proceed
    if (x, i) not in self.memo:
      count = 0
      if i < self.n:
        for xnext in (x + self.nums[i], x  - self.nums[i]):
          if i + 1 == self.n or xnext - self.crsm[i + 1] <= self.S <= xnext + self.crsm[i + 1]:
            count += self.backtrack(xnext, i + 1)
      self.memo[(x, i)] = count
    return self.memo[(x, i)]
  def findTargetSumWays(self, nums: List[int], S: int) -> int:
    # nums
    self.nums, self.n, self.S = nums, len(nums), S
    # crsm: cumulative right sum
    self.crsm = nums.copy()
    for i in range(1, self.n):
      self.crsm[-(i + 1)] += self.crsm[-i]
    # memo
    self.memo = {}
    # memo init
    self.memo[(self.S, self.n)] = 1
    # backtrack with memo
    return self.backtrack(0, 0)

class Solution:
  def findTargetSumWays(self, nums: List[int], S: int) -> int:
    """S = sum(xi) - sum(xj), T = sum(xi) + sum(xj), xi with +, xj with -, => sum(xi) = (T + S) // 2.
    """
    T = sum(nums)
    if S > T or (T + S) % 2 == 1:
      return 0
    W = (T + S) // 2
    dp = [0] * (W + 1)
    dp[0] = 1
    for num in nums:
      for i in range(W, num - 1, -1):
        dp[i] += dp[i - num]
    return dp[W]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1, 1, 1, 1, 1], 3),
    ([14,23,35,48,10,39,34,40,36,45,11,14,41,6,4,17,42,22,0,35], 44),
  ]
  rslts = [solver.findTargetSumWays(nums, S) for nums, S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  
