from typing import List
from functools import reduce, lru_cache

import operator

class Solution:
  @lru_cache(None)
  def recursive(self, i, k):
    # i: index, k: num of 1s
    if i + k == self.n:
      return reduce(operator.__mul__, self.prob[i:])
    if k == 0:
      return reduce(operator.__mul__, [1 - x for x in self.prob[i:]])
    return self.prob[i] * self.recursive(i + 1, k - 1) + (1 - self.prob[i]) * self.recursive(i + 1, k)
  def probabilityOfHeads(self, prob: List[float], target: int) -> float:
    self.prob, self.n = prob, len(prob)
    self.recursive.cache_clear()
    return self.recursive(0, target)

class Solution:
  def probabilityOfHeads(self, prob, target):
    dp = [1] + [0] * target
    for p in prob:
      for k in range(target, -1, -1):
        dp[k] = (dp[k - 1] if k else 0) * p + dp[k] * (1 - p)
    return dp[target]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([0.4], 1),
    ([0.5,0.5,0.5,0.5,0.5], 0),
    ([0.1,0.2,0.3,0.4,0.5], 2),
    ([0.1,0.2,0.3,0.4,0.5], 3),
  ]
  rslts = [solver.probabilityOfHeads(prob, target) for prob, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
