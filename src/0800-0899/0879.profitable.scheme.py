from typing import List

class Solution:
  def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
    # dynamic programming
    # dp[i][j]: num of scheme with i people to profit j (at j == P, it means P or P+)
    dp = [[0] * (P + 1) for _ in range(G + 1)]
    # dp[i][j]
    dp[0][0] = 1
    for g, p in zip(group, profit):
      for i in range(G, g - 1, -1):
        for j in range(P, -1, -1):
          dp[i][j] += dp[i - g][max(0, j - p)]
    # return sum(dp[:][P]) % (10 ** 9 + 7)
    return sum(list(zip(*dp))[-1]) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (5, 3, [2,2], [2,3]),
    (10, 5, [2,3,5], [6,7,8]),
  ]
  rslts = [solver.profitableSchemes(G, P, group, profit) for G, P, group, profit in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
