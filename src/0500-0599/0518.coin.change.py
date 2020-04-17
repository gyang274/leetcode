from typing import List

class Solution:
  def change(self, amount: int, coins: List[int]) -> int:
    """Q0039
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
      for x in range(coin, amount + 1):
        dp[x] += dp[x - coin]
    return dp[amount]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (5, [1,2,5]),
    (12, [1,2,5]),
  ]
  rslts = [solver.change(amount, coins) for amount, coins in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")