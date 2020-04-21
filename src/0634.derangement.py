class Solution:
  def findDerangement(self, n: int) -> int:
    # f(n) = (n - 1) * (f(n - 1) + f(n - 2))
    if n < 2:
      return 0
    dp = [0] * (n + 1)
    dp[1] = 0
    dp[2] = 1
    for i in range(3, n + 1):
      dp[i] = ((i - 1) * (dp[i - 1] + dp[i - 2])) % (10 ** 9 + 7)
    return dp[n]

class Solution:
  def findDerangement(self, n: int) -> int:
    # f(n) = (n - 1) * (f(n - 1) + f(n - 2))
    if n < 2:
      return 0
    d1, d2 = 1, 0
    for i in range(3, n + 1):
      d1, d2 = ((i - 1) * (d1 + d2)) % (10 ** 9 + 7), d1
    return d1