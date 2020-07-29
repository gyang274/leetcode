from typing import List

class Solution:
  def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
    # dynamic programming, O(NK)
    dp = [0] * (len(A) + 1)
    for i in range(len(A)):
      xmax = 0
      for k in range(1, min(i + 1, K) + 1):
        xmax = max(xmax, A[i - k + 1])
        dp[i] = max(dp[i], dp[i - k] + xmax * k)
    return dp[len(A) - 1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,15,14,3], 3),
    ([3,15,14,2], 3),
    ([2,14,15,3], 3),
    ([3,14,15,2], 3),
    ([1,15,7,9,2,5,10], 3),
    ([10,15,7,9,2,5,1], 3),
  ]
  rslts = [solver.maxSumAfterPartitioning(A, K) for A, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
