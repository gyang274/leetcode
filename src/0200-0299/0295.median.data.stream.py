import heapq

class MedianFinder:
  """Solutions:
    1. add O(1), find median O(NlogN) by sort.
    2. add O(logN) + O(N) by insertion on sorted array, O(N) as potential move of array, and find median O(1).
    3. add O(5*logN) by keep 2 priority queue for >=median and <median, find median O(1).
  """
  def __init__(self):
    """initialize your data structure here.
    """
    self.upper = []
    self.lower = []
    
  def addNum(self, num: int) -> None:
    heapq.heappush(self.upper, num)
    # make sure size balance, at most 1 operation per addNum()
    while len(self.upper) > len(self.lower) + 1:
      x = heapq.heappop(self.upper)
      # push -x to lower so the smallest -x is the largest x
      heapq.heappush(self.lower, -x)
    if self.lower:
      # make sure values in upper >= values in lower, at most 2 x 2 operation per addNum()
      while self.upper[0] < -self.lower[0]:
        xl, xu = heapq.heappop(self.upper), heapq.heappop(self.lower)
        heapq.heappush(self.upper, -xu)
        heapq.heappush(self.lower, -xl)
    print(self.upper, self.lower)

  def findMedian(self) -> float:
    # if len(self.upper) == 0:
    #   # raise error?
    #   return None
    if len(self.upper) == len(self.lower):
      # x = self.upper[0]
      # y = -self.lower[0]
      # return (x + y) / 2.0
      return (self.upper[0] - self.lower[0]) / 2.0
    else:
      # len(self.upper) == len(self.lower) + 1
      return self.upper[0]
