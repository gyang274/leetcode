class Solution:
  def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    i, j, satified = 0, 0, 0
    while i < len(g) and j < len(s):
      if g[i] <= s[j]:
        satified += 1
        i += 1
        j += 1
      else:
        j += 1
    return satified
