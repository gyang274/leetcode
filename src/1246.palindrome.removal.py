from typing import List

class Solution:
  def minimumMoves(self, arr: List[int]) -> int:
    # split expansion, TC: O(N^3), SC: O(N^2)
    n = len(arr)
    # dp[i][j], min moves for arr[i:(j+1)]
    # dp[i][j] = min(dp[i][k], dp[(k+1):j]), all i < k < j
    # key: must know all internals of (i, k) and (k + 1, j) before (i, j)
    dp = [[n] * n for _ in range(n)]
    for j in range(n):
      for i in range(j, -1, -1):
        if arr[i] == arr[j]:
          dp[i][j] = 1 if i + 1 >= j - 1 else dp[i + 1][j - 1]
        for k in range(i, j):
          dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
    return dp[0][n - 1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2,3,1,4],
  ]
  rslts = [solver.minimumMoves(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
