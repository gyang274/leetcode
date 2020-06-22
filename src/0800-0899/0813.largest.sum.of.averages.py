from typing import List

class Solution:
  def largestSumOfAverages(self, A: List[int], K: int) -> float:
    n = len(A)
    for i in range(1, n):
      A[i] += A[i - 1]
    # since A[i] > 1, split of k will always achieve larger sum than split of k - 1
    # dp(i, k) = max(dp(j, k - 1) + mean(A[(j + 1):(i + 1))])), j < i, split A[:i] into k partition
    dp = [[0] * K for _ in range(n)]
    for i in range(n):
      dp[i][0] = A[i] / (i + 1)
      for k in range(1, K):
        if k >= i:
          dp[i][k] = A[i]
        else:
          dp[i][k] = max([dp[j][k - 1] + (A[i] - A[j]) / (i - j) for j in range(i)])
    return dp[n - 1][K - 1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([9,1,2,3,9], 3),
  ]
  rslts = [solver.largestSumOfAverages(A, K) for A, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
