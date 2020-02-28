class Solution:
  def backtrack(self, n):
    if n not in self.memo:
      # closest perfect square's root
      r = int(n ** 0.5)
      if n == r ** 2:
        self.memo[n] = 1
      else:
        # upper bound, all 1
        self.memo[n] = n
        for s in range(1, r + 1):
          self.memo[n] = min(self.backtrack(n - s ** 2) + 1, self.memo[n])
    return self.memo[n]
  def numSquares(self, n: int) -> int:
    """backtrack.
    """
    self.memo = {0: 0}
    self.backtrack(n)
    return self.memo[n]

class Solution:
  def numSquares(self, n: int) -> int:
    """dynamic programming.
    """
    dp = [i for i in range(n + 1)]
    for i in range(1, n + 1):
      j = int(i ** 0.5)
      if i == j ** 2:
        dp[i] = 1
      else:
        for k in range(1, j + 1):
          dp[i] = min(dp[i - k ** 2] + 1, dp[i])
    return dp[n]

class Solution:
  def backtrack(self, n):
    if n not in self.memo:
      m = int(n ** 0.5)
      if n == m ** 2:
        self.memo[n] = 1
      else:
        self.memo[n] = n
        for s in range(1, m + 1):
          # only requires up to sqrt(n), instead of n
          self.memo[n] = min(self.backtrack(n % s ** 2) + (n // (s ** 2)), self.memo[n])
    return self.memo[n]
  def numSquares(self, n: int) -> int:
    """backtrack.
      improvement: only recursive up to sqrt(n) instead all 1, .., n.
    """
    self.memo = {0: 0}
    self.backtrack(n)
    return self.memo[n]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 2, 3, 4, 5, 8, 12, 17, 48, 85, 5374, 6922,
  ]
  rslts = [solver.numSquares(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")