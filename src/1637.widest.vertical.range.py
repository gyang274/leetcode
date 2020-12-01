class Solution:
  def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
    xs = sorted(list(set([x for x, y in points])))
    return max(x2 - x1 for x1, x2 in zip(xs[:-1], xs[1:]))
        