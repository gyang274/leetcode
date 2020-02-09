from typing import List

class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    """dynamic programming 1d:
      dp[i] represents minTotal of all path to j, loop over triangle each level i and keep status of j only.
    """
    # if not triangle:
    #   return 0
    n = len(triangle) 
    # dp = [0] * len(triangle[-1])
    dp = [0] * n
    dp[0] = triangle[0][0]
    for i in range(1, n):
      dp[i] = dp[i - 1] + triangle[i][i]
      for j in range(i - 1, 0, -1):
        dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]
      dp[0] += triangle[i][0]
    return min(dp)

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3],
    ],
    [[-1],[-2,-3]],
  ]
  rslts = [solver.minimumTotal(triangle) for triangle in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  