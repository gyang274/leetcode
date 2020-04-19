import heapq

class Solution:
  def maxDistance(self, arrays: List[List[int]]) -> int:
    qmin = [(x[0], i) for i, x in enumerate(arrays)]
    qmax = [(-x[-1], -i) for i, x in enumerate(arrays)]
    heapq.heapify(qmin)
    heapq.heapify(qmax)
    xmax, imax = heapq.heappop(qmax)
    xmin, imin = heapq.heappop(qmin)
    if imax + imin == 0:
      x2max, i2max = heapq.heappop(qmax)
      x2min, i2min = heapq.heappop(qmin)
      return max(abs(xmin + x2max), abs(x2min + xmax))
    else:
      return abs(xmin + xmax)
