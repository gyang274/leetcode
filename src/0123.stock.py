from typing import List

# class Solution:
#   def maxProfit(self, prices: List[int]) -> int:
#     """dynamic programming: dp[i][k] max profit at day i - 1 with k transactions.
#       dp[i][k] = max(dp[i - 1][k], dp[i - j - 1][k - 1] + (prices[i - 1] - prices[i - 1 - j]), all 1 < j < i)
#     """
#     n = len(prices)
#     dp = [[0] * 3 for _ in range(n + 1)]
#     for i in range(1, n + 1):
#       for k in range(1, 3):
#         dp[i][k] = dp[i - 1][k]
#         for j in range(1, i):
#           dp[i][k] = max(dp[i][k], dp[i - j - 1][k - 1] + prices[i - 1] - prices[i - 1 - j])
#       print(dp)
#     return dp[n][2]

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    """dynamic programming: dp[i][k] max profit at day i - 1 with k transactions.
        dp[i][k] = max(dp[i - 1][k], dp[i - j - 1][k - 1] + (prices[i - 1] - prices[i - 1 - j]), all 1 < j < i)
      improvement:
        at day i - 1, price[i - 1] is fixed, so dp[i][k] = max(, ..) is equivalent to find
        max(dp[i - j - 1][k - 1] - prices[i - 1 - j]), e.g., unrealized profit or say buy and hold from day i - 1 -j,
        in previous setting, this unrealized profit is re-calculated day by day, instead, keep a umax as memorization
    """
    n = len(prices)
    dp = [[0] * 3 for _ in range(n + 1)]
    umax = [0, -2147483648, -2147483648]
    for i in range(2, n + 1):
      for k in range(1, 3):
        umax[k] = max(umax[k], dp[i - 2][k - 1] - prices[i - 2])
        dp[i][k] = max(dp[i - 1][k], prices[i - 1] + umax[k])
    return dp[n][2]

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    """status machine: 
        s1 buy or hold, s2 sell previous brought or hold, 1st transaction.
        s3 buy or hold from s2, s4 sell or hold w.r.t s3, 2nd transaction.
    """
    s1, s2, s3, s4 = -2147483648, 0, -2147483648, 0
    for x in prices:
      s1 = max(s1, -x)
      s2 = max(s2, s1 + x)
      s3 = max(s3, s2 - x)
      s4 = max(s4, s3 + x)
    return s4

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [1,2,3,4,5],
    [7,6,4,3,1],
    [7,1,5,3,6,4],
    [3,3,5,0,0,3,1,4],
  ]
  rslts = [solver.maxProfit(prices) for prices in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}") 