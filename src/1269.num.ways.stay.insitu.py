from functools import lru_cache

class Solution:
  @lru_cache(None)
  def recursive(self, x, i):
    # x: steps remain, i: current position.
    if x == i:
      return 1
    count = 0
    if x > 0:
      # stay
      count += self.recursive(x - 1, i)
      # left
      if i - 1 >= 0:
        count += self.recursive(x - 1, i - 1)
      # right
      if i + 1 < self.L:
        count += self.recursive(x - 1, i + 1)
    return count % (10 ** 9 + 7)
  def numWays(self, steps: int, arrLen: int) -> int:
    self.L = arrLen
    return self.recursive(steps, 0)

class Solution:
  def numWays(self, steps: int, arrLen: int) -> int:
    dp = [0, 1]
    r, M = min(arrLen, steps // 2 + 1), 10 ** 9 +  7
    for s in range(steps):
      dp[1:] = [sum(dp[(i - 1):(i + 2)]) % M for i in range(1, min(r + 1, s + 3))]
    return dp[1] % M

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, 2),
    (2, 4),
    (4, 2),
    (8, 5),
  ]
  rslts = [solver.numWays(steps, arrLen) for steps, arrLen in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
