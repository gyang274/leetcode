from typing import List

class Solution:
  def minimumEffort(self, tasks: List[List[int]]) -> int:
    # q: task sorted by extra energy required
    q = sorted((y - x, x) for x, y in tasks)
    # r: extra energy required
    # d: extra energy reserved
    r, d = 0, 0
    for e, x in q:
      r += max(0, e - d - r)
      d += x
    return d + r
