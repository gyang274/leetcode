class Solution:
  def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    if not ops:
        return m * n
    mx, nx = map(min, zip(*ops))
    return mx * nx