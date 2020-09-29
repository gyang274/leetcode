from typing import List
from functools import lru_cache

class Solution:
  @lru_cache(None)
  def recursive(self, i, k):
    if k == 1:
      return max(self.x[i:])
    m, ans = float('-inf'), float('inf')
    for j in range(i, self.n + 1 - k):
      m = max(m, self.x[j])
      ans = min(ans, m + self.recursive(j + 1, k - 1))
    return ans
  def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    # split the array into d subarray, want to minimize sum(max(subarrays))
    self.x, self.n = jobDifficulty, len(jobDifficulty)
    if self.n < d:
      return -1
    self.recursive.cache_clear()
    return self.recursive(0, d)

class Solution:
  def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    # stack, TC: O(ND), SC: O(N)
    A, n = jobDifficulty, len(jobDifficulty)
    dp0, dp1 = [float('inf')] * n, [0] * n
    if n < d:
      return -1
    for d in range(d):
      stack = []
      for i in range(d, n):
        dp1[i] = (dp0[i - 1] + A[i]) if i else A[i]
        while stack and A[stack[-1]] <= A[i]:
          j = stack.pop()
          dp1[i] = min(dp1[i], dp1[j] - A[j] + A[i])
        if stack:
          dp1[i] = min(dp1[i], dp1[stack[-1]])
        stack.append(i)
      dp0, dp1 = dp1, [0] * n
    return dp0[-1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([6,5,4,3,2,1], 2),
    ([7,1,4,2,8,5], 3),
    ([11,111,22,222,33,333,44,444], 5),
  ]
  rslts = [solver.minDifficulty(jobDifficulty, d) for jobDifficulty, d in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
