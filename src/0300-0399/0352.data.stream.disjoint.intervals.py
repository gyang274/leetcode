class SummaryRanges:
  def __init__(self):
    self.x = list()
  def addNum(self, val: int) -> None:
    l, r = 0, len(self.x)
    seen = False
    while l < r:
      m = l + (r - l) // 2
      # lower and upper
      ml, mu = self.x[m]
      if ml <= val <= mu:
        seen = True
        break
      elif val < ml:
        r = m
      else:
        l = m + 1
    if not seen:
      # merge left, merge right
      okl = l > 0 and self.x[l - 1][1] == val - 1
      okr = l < len(self.x) and val + 1 == self.x[l][0]
      if okl and okr:
        rl, rr = self.x.pop(l)
        self.x[l - 1][1] = rr
      elif okl:
        self.x[l - 1][1] += 1
      elif okr:
        self.x[l][0] -= 1
      else:
        self.x.insert(l, [val, val])
  def getIntervals(self) -> List[List[int]]:
    return self.x

# Lazy merge when getIntervals() called, with heapq.
import heapq

class SummaryRanges(object):
  def __init__(self):
    # seen make sure no duplicate keys in heapq
    self.seen = set()
    self.intervals = []
  def addNum(self, val: int) -> None:
    if val not in self.seen:
      self.seen.add(val)
      heapq.heappush(self.intervals, [val, val])
  def getIntervals(self) -> List[List[int]]:
    x = []
    while self.intervals:
      v = heapq.heappop(self.intervals)
      if x and v[0] <= x[-1][1] + 1:
        x[-1][1] = max(x[-1][1], v[1])
      else:
        x.append(v)
    self.intervals = x
    return self.intervals