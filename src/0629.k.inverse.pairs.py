class Solution:
  def recursive(self, n, k):
    """recursive over 1st element value, nums[0] = v means v - 1 reverse pairs.
    """
    if (n, k) not in self.memo:
      if n == 0:
        self.memo[(n, k)] = 0
      elif k == 0:
        self.memo[(n, k)] = 1
      elif k > (n - 1) * n // 2:
        # max num of inverse: (n - 1) * n // 2
        self.memo[(n, k)] = 0
      elif k == (n - 1) * n // 2:
        self.memo[(n, k)] = 1
      else:
        self.memo[(n, k)] = 0
        # recursive over 1st element value, nums[0] = v means v - 1 reverse pairs.
        # (n, k), nums[0] = v => (n - 1, k - (v - 1))
        # 0 <= k - (v - 1) <= (n - 1) * (n - 2) // 2
        # k - (n - 1) * (n - 2) // 2 + 1 <= v <= k + 1
        # max(1, k - (n - 1) * (n - 2) // 2 + 1) <= v <= min(k + 1, n)
        # so, max(0, k - (n - 1) * (n - 2) // 2) <= v - 1 < min(k + 1, n)
        for i in range(max(0, k - (n - 1) * (n - 2) // 2), min(k + 1, n)):
          self.memo[(n, k)] += self.recursive(n - 1, k - i)
        self.memo[(n, k)] %= (10 ** 9 + 7)
    return self.memo[(n, k)]
  def kInversePairs(self, n: int, k: int) -> int:
    self.memo = {}
    return self.recursive(n, k)

class Solution:
  def kInversePairs(self, n: int, k: int) -> int:
    # dp[i][j]: inverse pairs (i + 1, j)
    dp = [[0] * (k + 1) for _ in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
      for j in range(min((i + 1) * i // 2, k) + 1):
        dp[i][j] = sum(dp[i - 1][max(0, j - i):min(j + 1, (i + 1) * i // 2 + 1)]) % (10 ** 9 + 7)
    return dp[n - 1][k]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 0),
    (1, 1),
    (2, 3),
    (5, 8),
    (42, 85),
    (1000, 1000),
  ]
  rslts = [solver.kInversePairs(n, k) for n, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
