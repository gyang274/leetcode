from typing import List
from collections import defaultdict, Counter

class Solution:
  def isReflected(self, points: List[List[int]]) -> bool:
    """O(N), assume strict not only points position but also num, e.g., [[-1,0],[1,0],[1,0]] is false.
    """
    # if reflected by y-axis, must reflected all xs w.r.t each y
    ys = defaultdict(list)
    for x, y in points:
      ys[y].append(x)
    # if reflected by y-axis, must reflected all xs w.r.t each y, so all y should have same reflection point r
    r = None
    for y in ys:
      r = sum(ys[y]) / len(ys[y]) if r is None else r
      if not r == sum(ys[y]) / len(ys[y]):
        return False
      # verify the reflection of xs at each y
      xs = Counter(ys[y])
      for x in xs:
        z = 2 * r - x
        if not (z in xs and xs[x] == xs[z]):
          return False
    return True

class Solution:
  def isReflected(self, points: List[List[int]]) -> bool:
    """O(N), assume loose only points position, e.g., [[-1,0],[1,0],[1,0]] is true.
    """
    # if reflected by y-axis, must reflected all xs w.r.t each y
    ys = defaultdict(set)
    for x, y in points:
      ys[y].add(x)
    # if reflected by y-axis, must reflected all xs w.r.t each y, so all y should have same reflection point r
    r = None
    for y in ys:
      r = sum(ys[y]) / len(ys[y]) if r is None else r
      if not r == sum(ys[y]) / len(ys[y]):
        return False
      # verify the reflection of xs at each y
      for x in ys[y]:
        if 2 * r - x not in ys[y]:
          return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[-1,0],[1,0]],
    [[-1,0],[1,0],[0,0]],
    [[-1,0],[1,0],[1,0]],
    [[-1,0],[1,0],[1,0],[2,0]],
    [[-1,0],[1,0],[1,0],[3,0]],
  ]
  rslts = [solver.isReflected(points) for points in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
