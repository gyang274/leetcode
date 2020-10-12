from typing import List

import bisect

class Solution:
  def numTeams(self, rating: List[int]) -> int:
    n = len(rating)
    # prefix
    # prefix[j]: num of ratings s.t. rating[i] < rating[j], i < j
    preval, prefix = [], [0] * n
    for i in range(n):
      prefix[i] = bisect.bisect(preval, rating[i])
      bisect.insort(preval, rating[i])
    # suffix
    # suffix[j]: num of ratigns s.t. rating[j] < rating[k], j < k
    sufval, suffix = [], [0] * n
    for i in range(n - 1, -1, -1):
      suffix[i] = len(sufval) - bisect.bisect(sufval, rating[i])
      bisect.insort(sufval, rating[i])
    count = 0
    for i in range(1, n - 1):
      count += (prefix[i] * suffix[i]) + (i - prefix[i]) * (n - 1 - i - suffix[i])
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,1,3],
    [1,2,3,4],
    [2,5,3,4,1],
  ]
  rslts = [solver.numTeams(rating) for rating in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
