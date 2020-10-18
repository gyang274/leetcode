from typing import List
from functools import lru_cache

class Solution:
  @lru_cache(None)
  def recursive(self, i, k):
    pass
  def main(self, nums: List[int], k: int) -> int:
    self.recursive.cache_clear()
    return self.recursive(0, k)
