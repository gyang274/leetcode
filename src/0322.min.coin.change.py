from typing import List

class Solution:
  def _getGCD(self, x, y):
    while y:
      x, y = y, x % y
    return x
  def _getLCM(self, x, y):
    return x * y // self._getGCD(x, y)
  def recursive(self, amount):
    if amount not in self.memo:
      n = -1
      for x in self.coins:
        if amount >= x:
          nx = self.recursive(amount - x)
          if nx > -1:
            n = min(nx + 1, n) if n > -1 else nx + 1
      self.memo[amount] = n
    return self.memo[amount]
  def coinChange(self, coins: List[int], amount: int) -> int:
    """in case a given coins set with multiple calls on coin change, we should init with all possible change up to the
      least common denominator (LCD) of coins bases, any value > LCD should be xLCD + reminder, which is known already.
    """
    self.coins = [x for x in coins if x > 0]
    self.coins.sort(reverse=True)
    if not self.coins:
      return -1
    self.memo = {0: 0}
    coinsLCM = 1
    for x in self.coins:
      coinsLCM = self._getLCM(coinsLCM, x)
    if amount >= coinsLCM:
      n = self.recursive(coinsLCM)
      r = self.recursive(amount % coinsLCM)
      # if n > -1 and r > -1: # n must be > -1
      if r > -1:
        return (amount // coinsLCM) * n + r 
      else:
        return -1
    return self.recursive(amount)

class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
      for x in range(coin, amount + 1):
        dp[x] = min(dp[x - coin] + 1, dp[x])
    return dp[amount] if dp[amount] < float('inf') else -1

class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    level = seen = {0}
    n = 0
    while level:
      if amount in level:
        return n
      # level contains all amounts can be decomposed to n coins (but not any m < n) exactly
      level = {a + c for a in level for c in coins if a + c <= amount} - seen
      seen |= level
      n += 1
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2], 3),
    ([1, 2, 5], 9),
    ([1, 4, 6], 8),
    ([186, 419, 83, 408], 6249),
  ]
  rslts = [solver.coinChange(coins, amount) for coins, amount in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")