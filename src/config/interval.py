from typing import List

import bisect

class Interval:
  """Interval: module operates on [x, y) intervals.
    interval = Interval() with interval.ranges = [x1, y1, x2, y2, ..] means [xi, yi) are covered.
  """

  def __init__(self, ranges: List[int] = []):
    self.ranges = ranges

  def _insert(self, ranges: List[int], x: int, y: int) -> List[int]:
    """insert [x, y) into ranges.
    """
    if x >= y:
      raise ValueError("interval [x, y), must x < y.")
    # print(f"insert [{x}, {y}) into {ranges}")
    l = bisect.bisect_left(ranges, x)
    r = bisect.bisect_right(ranges, y)
    if l & 1:
      if r & 1:
        ranges = ranges[:l] + ranges[r:]
      else:
        ranges = ranges[:l] + [y] + ranges[r:]
    else:
      if r & 1:
        ranges = ranges[:l] + [x] + ranges[r:]
      else:
        ranges = ranges[:l] + [x, y] + ranges[r:]
    # print(f"->> {ranges}")
    return ranges

  def _remove(self, ranges: List[int], x: int, y: int) -> List[int]:
    """remove [x, y) from ranges.
    """
    if x >= y:
      raise ValueError("interval [x, y), must x < y.")
    # print(f"remove [{x}, {y}) from {ranges}")
    l = bisect.bisect_left(ranges, x)
    r = bisect.bisect_right(ranges, y)
    if l & 1:
      if r & 1:
        ranges = ranges[:l] + [x, y] + ranges[r:]
      else:
        ranges = ranges[:l] + [x] + ranges[r:]
    else:
      if r & 1:
        ranges = ranges[:l] + [y] + ranges[r:]
      else:
        ranges = ranges[:l] + ranges[r:]
    # print(f"->> {ranges}")
    return ranges

  def insert(self, x: int, y: int) -> None:
    """insert [x, y) into self.ranges.
    """
    self.ranges = self._insert(self.ranges, x, y)

  def remove(self, x: int, y: int) -> None:
    """remove [x, y) from self.ranges.
    """
    self.ranges = self._remove(self.ranges, x, y)

  def cover(self, x: int, y: int) -> bool:
    """query [x, y) from self.ranges, return [x, y) is all covered or not.
    """
    if x >= y:
      raise ValueError("interval [x, y), must x < y.")
    l = bisect.bisect_left(self.ranges, x)
    r = bisect.bisect_right(self.ranges, y)
    # print(f"query, [{x}, {y}), {l, r} from {self.ranges}")
    if l == len(self.ranges) or r == 0:
      return False
    if l & 1 == 0 and self.ranges[l] == x:
      l += 1
    if r & 1 == 0 and self.ranges[r - 1] == y:
      r -= 1
    # print(f"query, [{x}, {y}), {l, r} from {self.ranges}")
    return l & 1 and l == r

  def _cross(self, ranges: List[int], x: int, y: int) -> List[int]:
    """cross [x, y) with ranges, return overlaps between ranges and [x, y) without modifying ranges.
    """
    if x >= y:
      raise ValueError("interval [x, y), must x < y.")
    l = bisect.bisect_left(ranges, x)
    r = bisect.bisect_right(ranges, y)
    # print(f"cross, [{x}, {y}), {l, r} from {ranges}")
    if l == len(ranges) or r == 0:
      return []
    if l & 1 and ranges[l] == x:
      l += 1
    if r & 1 and ranges[r - 1] == y:
      r -= 1
    # print(f"cross, [{x}, {y}), {l, r} from {ranges}")
    if l & 1:
      if r & 1:
        ranges = [x] + ranges[l:r] + [y]
      else:
        ranges = [x] + ranges[l:r]
    else:
      if r & 1:
        ranges = ranges[l:r] + [y]
      else:
        ranges = ranges[l:r]
    return ranges

  def cross(self, x: int, y: int) -> List[int]:
    """cross [x, y) with self.ranges, return overlaps between self.ranges and [x, y) without modifying self.ranges.
    """
    return self._cross(self.ranges, x, y)

  _union = _insert

  def union(self, x: int, y: int) -> List[int]:
    """union [x, y) with self.ranges, return the union of self.ranges and [x, y) without modifying self.ranges.
    """
    return self._union(self.ranges, x, y)

if __name__ == '__main__':
  interval = Interval()
  print(f"init: {interval.ranges=}")
  interval.insert(10, 20)
  interval.insert(30, 40)
  interval.remove(12, 14)
  interval.insert(26, 34)
  interval.remove(32, 37)
  print(f"insert/remove: {interval.ranges=}")
  print(f"cover: {interval.cover(10, 12)=}")
  print(f"cover: {interval.cover(12, 14)=}")
  print(f"cover: {interval.cover(12, 22)=}")
  print(f"cross: {interval.cross(14, 22)=}, {interval.ranges=}")
  print(f"cross: {interval.cross(11, 19)=}, {interval.ranges=}")
  print(f"cross: {interval.cross(23, 34)=}, {interval.ranges=}")
  print(f"union: {interval.union(14, 22)=}, {interval.ranges=}")
  print(f"union: {interval.union(11, 19)=}, {interval.ranges=}")
  print(f"union: {interval.union(23, 34)=}, {interval.ranges=}")