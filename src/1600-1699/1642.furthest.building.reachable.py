from typing import List

import heapq

class Solution:
  def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
    # delayed ladders use to replace most costly bricks seen.
    h, b, l = heights, bricks, ladders
    i, q, n = 0, [], len(heights)
    while i < n - 1:
      if h[i] < h[i + 1]:
        d = h[i] - h[i + 1]
        if b + d >= 0:
          # use bricks whenever possible
          b += d
          heapq.heappush(q, d)
        elif l > 0:
          # use ladders to replace most costly one jump seen
          l -= 1
          heapq.heappush(q, d)
          b += d - heapq.heappop(q)
        else:
          return i
      i += 1
    return n - 1
