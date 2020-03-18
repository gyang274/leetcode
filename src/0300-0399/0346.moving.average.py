from collections import deque

class MovingAverage:
  def __init__(self, size: int):
    self.n = size
    self.x = deque([])
  def next(self, val: int) -> float:
    # if self.n <= 0:
    #   return float('nan')
    if len(self.x) == self.n:
      self.x.popleft()
    self.x.append(val)
    return sum(self.x) / len(self.x)

class MovingAverage:
  def __init__(self, size: int):
    self.n = size
    self.x = deque([])
    self.xsum = 0
  def next(self, val: int) -> float:
    """sum in O(1).
    """
    # if self.n <= 0:
    #   return float('nan')
    head = 0
    if len(self.x) == self.n:
      head = self.x.popleft()
    self.x.append(val)
    self.xsum += val - head
    return self.xsum / len(self.x)

class MovingAverage:
  def __init__(self, size: int):
    self.i = 0
    self.n = size
    self.x = []
    self.xsum = 0
  def next(self, val: int) -> float:
    """sum in O(1), no pop().
    """
    # if self.n <= 0:
    #   return float('nan')
    head = 0
    if len(self.x) < self.n:
      self.x.append(val)
    else:
      head = self.x[self.i]
      self.x[self.i] = val
      self.i = (self.i + 1) % self.n
    self.xsum += val - head
    return self.xsum / len(self.x)