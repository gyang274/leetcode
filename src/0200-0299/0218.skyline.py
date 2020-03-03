from typing import List
from itertools import chain

class Solution:
  def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    # convert buildings from [[li, ri, hi], ..] to [[i, l, h, 0], [i, r, h, 1], ..]
    # xyz: x-coordinate l and r, y-coordinate height, z-coordinate in and out
    ixyzlist = list(chain.from_iterable(((i, l, h, -1), (i, r, h, 1)) for i, (l, r, h) in enumerate(buildings)))
    # sorted by x-coordinate l and r, 
    # then z-coordinate (get into < out from), 
    # then y-coordinate the higher one should first in last out
    ixyzlist.sort(key=lambda ixyz: (ixyz[1], ixyz[3], ixyz[2] * ixyz[3]))
    # maintain a max-stack zstack [(i, h, hmax), ..] (or priority-queue?) as in Q0155, Q0716?
    ymax, zstack, skyline = 0, {}, []
    for i, x, y, z in ixyzlist:
      # some building get into skyline
      if z == -1:
        if y > ymax:
          ymax = y
          skyline.append((x, ymax))
        zstack[i] = y
      # some building out from skyline
      else:
        y = zstack.pop(i)
        if y == ymax:
          if zstack:
            ymax = max(zstack.values())
            if ymax < y:
              skyline.append((x, ymax))
          else:
            ymax = 0
            skyline.append((x, ymax))
    return skyline

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,2,3],[2,5,3]],
    [[1,2,1],[1,2,2],[1,2,3]],
    [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]],
  ]
  rslts = [solver.getSkyline(buildings) for buildings in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")