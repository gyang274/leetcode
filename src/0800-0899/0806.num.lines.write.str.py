from typing import List

class Solution:
  def numberOfLines(self, widths: List[int], S: str) -> List[int]:
    # l, r: lines, last line residuals
    l, r = 1, 0
    for x in S:
      w = widths[ord(x) - ord('a')]
      if r + w > 100:
        l += 1
        r = w
      else:
        r += w
    return [l, r]