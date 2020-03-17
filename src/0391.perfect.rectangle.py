from typing import List

class Solution:
  def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
    # isRectangle if and only if no overlap and area match
    # no overlap can be considered as extreme points expansion
    # https://github.com/gyang274/gbp/blob/master/src/gbp2d_xp.cpp
    # a priority queue on y, and a priority queue on x for each y
    # no overlap can simply be all unique corners are overall corners
    _get_area = lambda x0, y0, x1, y1: (x1 - x0) * (y1 - y0)
    _get_corners = lambda x0, y0, x1, y1: set(((x0, y0), (x0, y1), (x1, y1), (x1, y0)))
    xmin, ymin, xmax, ymax, area, corners = float('inf'), float('inf'), float('-inf'), float('-inf'), 0, set([])
    for x0, y0, x1, y1 in rectangles:
      area += _get_area(x0, y0, x1, y1)
      corners ^= _get_corners(x0, y0, x1, y1)
      xmin = min(x0, xmin)
      ymin = min(y0, ymin)
      xmax = max(xmax, x1)
      ymax = max(ymax, y1)
    return area == _get_area(xmin, ymin, xmax, ymax) and corners == _get_corners(xmin, ymin, xmax, ymax)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      [1,1,3,3],
      [3,1,4,2],
      [3,2,4,4],
      [1,3,2,4],
      [2,3,3,4],
    ],
    [
      [1,1,2,3],
      [1,3,2,4],
      [3,1,4,2],
      [3,2,4,4],
    ],
    [
      [1,1,3,3],
      [3,1,4,2],
      [1,3,2,4],
      [3,2,4,4],
    ],
    [
      [1,1,3,3],
      [3,1,4,2],
      [1,3,2,4],
      [2,2,4,4],
    ],
  ]
  rslts = [solver.isRectangleCover(rectangles) for rectangles in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
