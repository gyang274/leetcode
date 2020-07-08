from typing import List
from collections import defaultdict

class Solution:
  def tallestBillboard(self, rods: List[int]) -> int:
    # dynamic programming, O(NS)
    # N = len(rods), S = sum(rods)
    # dp(i, j): max value acheived on left by use the i-th rod with difference j = left - right
    # dp(-1, 0) = 0
    # dp(i, j) = max(dp(i - 1, j), dp(i - 1, j - x) + x, dp(i - 1, j + x))
    dp = defaultdict(lambda: defaultdict(lambda: 0))
    dp[-1][0] = 0
    for i, x in enumerate(rods):
      for j in dp[i - 1]:
        dp[i][j] = max(dp[i][j], dp[i - 1][j]) # if j in dp[i] else dp[i - 1][j]
        dp[i][j - x] = max(dp[i][j - x], dp[i - 1][j]) # if j - x in dp[i] else dp[i - 1][j]
        dp[i][j + x] = max(dp[i][j + x], dp[i - 1][j] + x) # if j + x in dp[i] else dp[i - 1][j] + x
    return dp[len(rods) - 1][0]

class Solution:
  def tallestBillboard(self, rods: List[int]) -> int:
    # meet in the middle, reduce TC: O(3^N) => O(3^(N/2))
    def make(A):
      # state of (left, right) for a set of rods
      state = {(0, 0)}
      for x in A:
        state |= ({(l + x, r) for l, r in state} | {(l, r + x) for l, r in state})
      # delta: max score achieved for each delta
      delta = {}
      for l, r in state:
        delta[l - r] = max(delta.get(l - r, 0), l)
      return delta
    # meet in the middle
    n = len(rods)
    ldelta = make(rods[:(n // 2)])
    rdelta = make(rods[(n // 2):])
    ans = 0
    for d in ldelta:
      if -d in rdelta:
        ans = max(ans, ldelta[d] + rdelta[-d])
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2],
    [1,2,3],
    [1,2,3,4],
    [1,2,3,4,5],
    [1,2,3,4,5,6],
  ]
  rslts = [solver.tallestBillboard(rods) for rods in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
