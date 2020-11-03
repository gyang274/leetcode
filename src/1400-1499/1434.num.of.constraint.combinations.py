from typing import List
from collections import defaultdict

class Solution:
  def numberWays(self, hats: List[List[int]]) -> int:
    n = len(hats)
    # bitmask
    # TC: O(n * 40 * 2^40)
    dp = defaultdict(lambda: defaultdict(lambda: 0))
    # init
    dp[-1][0] = 1
    # main
    for i in range(n):
      for x in hats[i]:
        m = 1 << (x - 1)
        for k in dp[i - 1]:
          if not k & m:
            dp[i][k | m] += dp[i - 1][k]
    return sum(dp[n - 1][k] for k in dp[n - 1]) % (10 ** 9 + 7)

class Solution:
  def numberWays(self, hats: List[List[int]]) -> int:
    # note: 1 <= n <= 10, assign hat to people, 
    # instead of assign people to hat (above, TLE)
    n = len(hats)
    # bitmask
    # TC: O(40 * n * 2^n)
    H = 40
    # hp: hp[i] list of people can take i-th hat
    hp = [[] for _ in range(H)]
    for p, hs in enumerate(hats):
      for h in hs:
        hp[h - 1].append(p)
    dp = defaultdict(lambda: defaultdict(lambda: 0))
    dp[-1][0] = 1
    for h in range(H):
      # no one take this hat
      for k in dp[h - 1]:
        dp[h][k] += dp[h - 1][k]
      # someone take this hat
      for p in hp[h]:
        for k in dp[h - 1]:
          if not k & (1 << p):
            dp[h][k | (1 << p)] += dp[h - 1][k]
    return dp[H - 1][(1 << n) - 1] % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]],
    [[1,2,4,6,7,8,9,11,12,13,14,15,16,18,19,20,23,24,25],[2,5,16],[1,4,5,6,7,8,9,12,15,16,17,19,21,22,24,25],[1,3,6,8,11,12,13,16,17,19,20,22,24,25],[11,12,14,16,18,24],[2,3,4,5,7,8,13,14,15,17,18,21,24],[1,2,6,7,10,11,13,14,16,18,19,21,23],[1,3,6,7,8,9,10,11,12,14,15,16,18,20,21,22,23,24,25],[2,3,4,6,7,10,12,14,15,16,17,21,22,23,24,25]],
  ]
  rslts = [solver.numberWays(hats) for hats in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
