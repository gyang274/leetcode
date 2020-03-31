from typing import List
from collections import defaultdict

class Solution:
  def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    """dynamic programming: dp[i][(rm, rn)] = max(dp[i - 1][(rm, rn)], dp[i - 1][(rm - sm, rn - sn)] + 1),
      all 0 <= rm <= m, 0 <= rn <= n.
    """
    dp = [defaultdict(lambda: 0) for _ in range(len(strs) + 1)]
    for i in range(len(strs)):
      sm, sn = strs[i].count("0"), strs[i].count("1")
      # print(f"{i=}, {sm=}, {sn=}")
      for rm in range(0, m + 1):
        for rn in range(0, n + 1):
          dp[i + 1][(rm, rn)] = dp[i][(rm, rn)]
          if rm >= sm and rn >= sn:
            dp[i + 1][(rm, rn)] = max(dp[i + 1][(rm, rn)], dp[i][(rm - sm, rn - sn)] + 1)
      # print(f"{i=}, {dp[i + 1]=}")
    return dp[len(strs)][(m, n)]

class Solution:
  def recursive(self, m, n, k):
    self.mn = max(self.mn, k)
    pareto = set([])
    for sm, sn in self.keys:
      inPareto = False
      if not pareto:
        inPareto = True
      else:
        for pm, pn in pareto:
          if (sm < pm or sn < pn):
            inPareto = True
            break
      if inPareto:
        pareto.add((sm, sn))
        if (sm <= m and sn <= n) and (self.ss[(sm, sn)] > 0):
          self.ss[(sm, sn)] -= 1
          self.recursive(m - sm, n - sn, k + 1)
          self.ss[(sm, sn)] += 1
    return None
  def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    """constraint dfs, if sm1 <= sm2 and sn1 <= sn2 then (sm1, sn1) goes before (sm2, sn2).
    """
    self.ss = defaultdict(lambda: 0)
    for s in strs:
      self.ss[(s.count("0"), s.count("1"))] += 1
    self.keys = list(self.ss.keys())
    self.keys.sort(key=lambda mn: mn[0] + mn[1])
    # single 0 and single 1 are must have
    m0 = min(m, self.ss.pop((1, 0))) if (1, 0) in self.ss else 0
    m -= m0
    n0 = min(n, self.ss.pop((0, 1))) if (0, 1) in self.ss else 0
    n -= n0
    # go dfs with pareto frontier
    self.mn = 0
    self.recursive(m, n, 0)
    return self.mn + m0 + n0

class Solution:
  def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    """dynamic programming: dp[i][(rm, rn)] = max(dp[i - 1][(rm, rn)], dp[i - 1][(rm - sm, rn - sn)] + 1),
      all 0 <= rm <= m, 0 <= rn <= n.
    """
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for s in strs:
      sm, sn = s.count("0"), s.count("1")
      for rm in range(m, sm - 1, -1):
        for rn in range(n, sn - 1, -1):
          dp[rm][rn] = max(dp[rm][rn], dp[rm - sm][rn - sn] + 1)
    return dp[m][n]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["10", "1", "0"], 1, 1),
    (["10", "1", "0", "0001", "111001"], 5, 3),
  ]
  rslts = [solver.findMaxForm(strs, m, n) for strs, m, n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
