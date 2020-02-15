from typing import List

class Solution:
  def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    """dynameic programming.
      dp[i][j] represent the minHP required at (i, j), key is going through dungeon backwards.
    """
    INTEGER_MAX = 2147483647
    # n = len(dungeon)
    # if n == 0:
    #   return 0
    # m = len(dungeon[0])
    n, m = len(dungeon), len(dungeon[0])
    # init dp[][]
    dp = [[INTEGER_MAX] * (m + 1) for _ in range(n + 1)]
    dp[n][m - 1] = 1
    dp[n - 1][m] = 1
    # go through dungeon backwards
    for i in range(n - 1, -1, -1):
      for j in range(m - 1, -1, -1):
        hp = min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j]
        dp[i][j] = 1 if hp <= 0 else hp
    return dp[0][0] 

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[-2,-3,3],[-5,-10,1],[10,30,-5]],
  ]
  rslts = [solver.calculateMinimumHP(dungeon) for dungeon in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")