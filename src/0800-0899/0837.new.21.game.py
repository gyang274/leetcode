class Solution:
  def new21Game(self, N: int, K: int, W: int) -> float:
    # dp[i][j]: probability cards on hand = j at i-th round
    dp = [[0] * (N + 1) for i in range(K + 1)]
    # probability of proceeding to next round
    dp[0][0] = 1
    for i in range(1, K + 1):
      for j in range(1, K):
        dp[i][j] = sum(dp[i - 1][max(i - 1, j - W):j]) * 1 / W
      for j in range(K, N + 1):
        dp[i][j] = sum(dp[i - 1][max(i - 1, j - W):K]) * 1 / W + dp[i - 1][j]
    return sum(dp[K])

class Solution:
  def new21Game(self, N: int, K: int, W: int) -> float:
    """TC: O(N + W), SC: O(N + W).
    """
    # dp[i]: reverse the process, prob of win when start at i points.
    dp = [0] * (N + W + 1)
    # init
    for k in range(K, N + 1):
      dp[k] = 1.0
    # main
    # s(k) = dp[k + 1] + dp[k + 2] + .. + dp[k + W]
    # dp[k] = s(k) / W
    # s(k - 1) = s(k) + dp[k] - dp[k + W]
    s = min(N - K + 1, W)
    for k in range(K - 1, -1, -1):
      dp[k] = s / W
      s += dp[k] - dp[k + W]
    return dp[0]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (4, 1, 10),
    (10, 3, 10),
    (21, 17, 10),
    (9811, 8776, 1096),
  ]
  rslts = [solver.new21Game(N, K, W) for N, K, W in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
