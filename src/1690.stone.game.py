from typing import List

from functools import lru_cache

class Solution:
  @lru_cache(None)
  def score(self, i, j, s):
    if i == j:
      return 0
    return max(
      s - self.stones[i] - self.score(i + 1, j, s - self.stones[i]),
      s - self.stones[j] - self.score(i, j - 1, s - self.stones[j])
    )
  def stoneGameVII(self, stones: List[int]) -> int:
    self.stones = stones
    self.score.cache_clear()
    return self.score(0, len(stones) - 1, sum(stones))