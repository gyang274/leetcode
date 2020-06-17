class Solution:
  def superEggDrop(self, K: int, N: int) -> int:
    """dynamic programming, O(KN^2)
    """
    # dp(K, N) = min(max(dp(K, N - X), dp(K - 1, X - 1)), 1 <= X <= N) + 1
    dp = [[0] * (N + 1) for _ in range(K)]
    # init
    for j in range(N + 1):
      dp[0][j] = j
    # main
    for i in range(1, K):
      for j in range(1, N + 1):
        dp[i][j] = min(
          max(dp[i][j - k], dp[i - 1][k - 1]) for k in range(1, j + 1)
        ) + 1
    return dp[K - 1][N]

class Solution:
  def superEggDrop(self, K: int, N: int) -> int:
    """dynamic programming + monotonic increase property of dp(K, N), O(KN), Q0735.
    """
    dp = [[0] * (N + 1) for _ in range(K)]
    for j in range(N + 1):
      dp[0][j] = j
    for i in range(1, K):
      k = 1
      for j in range(1, N + 1):
        while k < j and dp[i][j - k] > dp[i - 1][k - 1]:
          k += 1
        dp[i][j] = min(dp[i][j - (k - 1)], dp[i - 1][k - 1]) + 1
    return dp[K - 1][N]

class Solution:
  def superEggDrop(self, K: int, N: int) -> int:
    """binary search + reverse problem as maximize N for given eggs K a moves M in O(K), O(KlogN)
    """
    # f(x) as maximum N can be determined by x moves with K eggs
    # f(x, K) = 1 + f(x - 1, K - 1) + f(x - 1, K) => f(x, K) = sum(choose(x, i), 1 <= i <= K)
    def f(x):
      ans, r = 0, 1
      for i in range(1, K + 1):
        r *= x - i + 1
        r //= i
        ans += r
        if ans >= N:
          break
      return ans
    # binary search
    l, r = 1, N
    while l < r:
      m = l + (r - l) // 2
      if f(m) < N:
        l = m + 1
      else:
        r = m
    return l

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 2),
    (2, 7),
    (3, 14),
    (23, 127),
  ]
  rslts = [solver.superEggDrop(K, N) for K, N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")