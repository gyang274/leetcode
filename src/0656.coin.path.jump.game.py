from typing import List

class Solution:
  def cheapestJump(self, A: List[int], B: int) -> List[int]:
    n = len(A)
    # dynamic programming
    dp = [[float("inf"), []] for _ in range(n)]
    # cost and path to index
    dp[0] = [A[0], [1]]
    for i in range(1, n):
      if A[i] > -1:
        for j in range(max(0, i - B), i):
          if dp[j][0] + A[i] < dp[i][0] or (dp[j][0] + A[i] == dp[i][0] and dp[j][1] + [i + 1] < dp[i][1]):
            dp[i] = [dp[j][0] + A[i], dp[j][1] + [i + 1]]
    return dp[n - 1][1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,4,-1,2], 1),
    ([1,2,4,-1,2], 2),
  ]
  rslts = [solver.cheapestJump(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
