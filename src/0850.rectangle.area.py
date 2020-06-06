from typing import List, Tuple

import itertools

class Solution:
  def rectangleArea(self, rectangles: List[List[int]]) -> int:
    """Line Sweep, TC: O(N^2logN).
    """
    M = 10 ** 9 + 7
    # imagine sweep y-axis along x-axis from xmin to xmax
    events = list(itertools.chain.from_iterable(
      ((x1, -1, y1, y2), (x2, 1, y1, y2)) for x1, y1, x2, y2 in rectangles
    ))
    events.sort()
    # maintain a sorted list of (y1, y2)
    active, x0, area = [], 0, 0
    # cover: total length covered by active (y1, y2) segments, O(N)
    def cover():
      l, y0 = 0, -1
      for y1, y2 in active:
        y0 = max(y0, y1)
        l += max(0, y2 - y0)
        y0 = max(y0, y2)
      return l
    # O(NlogN) * O(N)
    for x, io, y1, y2 in events:
      area += cover() * (x - x0)
      if io == -1:
        # open
        active.append((y1, y2))
        active.sort()
      else:
        # close
        active.remove((y1, y2))
      x0 = x
    return area % M

class Node(object):

  def __init__(self, init, ende, ys):
    self.init, self.ende = init, ende
    self.total = self.count = 0
    self._left = self._right = None
    self.ys = ys

  @property
  def mid(self):
    return (self.init + self.ende) // 2

  @property
  def left(self):
    self._left = self._left or Node(self.init, self.mid, self.ys)
    return self._left

  @property
  def right(self):
    self._right = self._right or Node(self.mid, self.ende, self.ys)
    return self._right

  def update(self, i, j, val):
    if i >= j:
      return 0
    if self.init == i and self.ende == j:
      self.count += val
    else:
      self.left.update(i, min(self.mid, j), val)
      self.right.update(max(self.mid, i), j, val)
    # total
    if self.count > 0:
      self.total = self.ys[self.ende] - self.ys[self.init]
    else:
      self.total = self.left.total + self.right.total
    return self.total

class Solution:
  def rectangleArea(self, rectangles: List[List[int]]) -> int:
    """Line Sweep using Segment Tree, TC: O(NlogN). Q0307, Q0308, Q0699.
    """
    M = 10 ** 9 + 7
    # imagine sweep y-axis along x-axis from xmin to xmax
    events = list(itertools.chain.from_iterable(
      ((x1, -1, y1, y2), (x2, 1, y1, y2)) for x1, y1, x2, y2 in rectangles
    ))
    events.sort()
    # segment tree over ys
    ys = list(itertools.chain.from_iterable((y1, y2) for x1, y1, x2, y2 in rectangles))
    ys.sort()
    # y's index in segment tree
    yi = {y: i for i, y in enumerate(ys)}
    # segment tree init with all 0s
    st = Node(0, len(ys) - 1, ys)
    # main
    x0, cover, area = 0, 0, 0
    for x, io, y1, y2 in events:
      area += cover * (x - x0)
      if io == -1:
        # open
        cover = st.update(yi[y1], yi[y2], 1)
      else:
        # close
        cover = st.update(yi[y1], yi[y2], -1)
      x0 = x
    return area % M

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0,1,1],[2,2,3,3]],
    [[0,0,2,2],[1,1,3,3]],
    [[0,0,1000000000,1000000000]],
    [[0,0,2,2],[1,0,2,3],[1,0,3,1]],
    [[25,20,70,27],[68,80,79,100],[37,41,66,76]],
  ]
  rslts = [solver.rectangleArea(rectangles) for rectangles in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")