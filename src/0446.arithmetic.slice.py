from typing import List
from collections import defaultdict

class Solution:
  def numberOfArithmeticSlices(self, A: List[int]) -> int:
    candidates = []
    for x in A:
      # 2, 2, infinity loop if append to candidates directly without extends 
      extends = []
      for seq in candidates:
        if len(seq[0]) == 1 or x - seq[0][-1] == seq[1]:
          extends.append([seq[0] + [x], x - seq[0][-1]])
      candidates.extend(extends)
      candidates.append([[x], None])
    # count num of arithmetic slice
    return sum([1 if len(seq[0]) > 2 else 0 for seq in candidates])

class Solution:
  def numberOfArithmeticSlices(self, A: List[int]) -> int:
    """dynamic programming.
    """
    # dp[i] = {d: count}, num of weak arithmetic slice (length >= 2) with diff ended with A[i]
    # ans: no count on arithmetic slice with length == 2
    ans, dp = 0, [defaultdict(lambda: 0) for _ in A]
    for i in range(len(A)):
      for j in range(i):
        d = A[i] - A[j]
        dp[i][d] += dp[j][d] + 1
        ans += dp[j][d]
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2, 2, 5, 8, 11],
    [2, 4, 6, 8, 10],
    [1, 2, 3, 5, 8, 11, 14, 17, 22, 42, 43, 46, 49, 52, 55, 58],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  ]
  rslts = [solver.numberOfArithmeticSlices(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")