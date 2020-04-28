from typing import List

import bisect

class Solution:
  def kEmptySlots(self, bulbs: List[int], K: int) -> int:
    lightOn = []
    for d, x in enumerate(bulbs, start=1):
      # binary search on lightOn
      i = bisect.bisect(lightOn, x)
      if i - 1 >= 0 and x - lightOn[i - 1] == K + 1:
        return d
      if i < len(lightOn) and lightOn[i] - x == K + 1:
        return d
      lightOn.insert(i, x)
    return -1

class Solution:
  def kEmptySlots(self, bulbs: List[int], K: int) -> int:
    # bulbs[i] = x, light x is on day (i + 1)
    # dayon[i] = x, light (i + 1) is on day x 
    dayon = [0] * len(bulbs)
    for d, x in enumerate(bulbs, start=1):
      dayon[x - 1] = d
    # one pass
    stack, dminK = [], len(bulbs) + 1
    for x, dx in enumerate(dayon):
      # light (x + 1) is on day d
      # if stack[-1][1] > d, it is off at day
      while stack and stack[-1][1] > dx:
        y, dy = stack.pop()
        # on day dy, y is on, and x is already on on day dx, dx < dy
        # all lights between y and x is off, dist between x and y is K
        if x - y == K + 1:
          dminK = min(dminK, dy)
      # on day dx, x is on, stack[-1][0] is already on on day stack[-1][1], and stack[-1][1] < dx
      # all lights between stack[-1][0] and x is off, dist between x and stack[-1][0] is K
      if stack and x - stack[-1][0] == K + 1:
        dminK = min(dminK, dx)
      stack.append((x, dx))
    return dminK if dminK <= len(bulbs) else -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([6,5,8,9,7,1,10,2,3,4], 2),
  ]
  rslts = [solver.kEmptySlots(bulbs, K) for bulbs, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")