from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    """dynamic programming:
      At day i, best buy and hold
        dp[i][0] = max(dp[i - 1][0], dp[i - 2][1] - x)
      At day i, best sell and rest
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + x)
    """
    dp = [[-2147483648, 0] for _ in range(len(prices) + 2)]
    for i, x in enumerate(prices):
      # best buy and hold at day i is hold over from i - 1 or buy and sell from 0
      # dp[i][0] = max(dp[i - 1][0], dp[i - 2][1] - x)
      # move to index day i using i + 2 to eliminate index < 0
      dp[i + 2][0] = max(dp[i + 1][0], dp[i][1] - x)
      # best sell and cooldown at day i is sell from previous buy and hold day i - 1 or cooldown from day i - 1
      # dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + x)
      # move to index day i using i + 2 to eliminate index < 0
      dp[i + 2][1] = max(dp[i + 1][1], dp[i + 1][0] + x)
    # return max profit from last day indexed as n - 1 + 2 = n + 1
    # return max(dp[len(prices) + 1])
    return max(dp[-1])

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    """status machine, with 3 status: sold, hold, rest.
    """
    hold, rest, sold = -2147483648, 0, 0
    for x in prices:
      hold = max(hold, rest - x)
      rest = max(rest, sold)
      sold = max(sold, hold + x)
    return max(sold, rest)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2,3,4,5],
    [1,2,3,4,2,5],
    [1,2,3,4,2,5,3,8],
  ]
  rslts = [solver.maxProfit(prices) for prices in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
        