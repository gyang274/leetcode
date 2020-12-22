from collections import deque

class FrontMiddleBackQueue:

  def __init__(self):
    # f, b: 1st and 2nd half of the queue
    # make sure len(f) == len(b) or len(f) == len(b) + 1
    self.f = deque([])
    self.b = deque([])
    # n, m: len(f) and len(b)
    # self.n = self.m = 0

  def pushFront(self, val: int) -> None:
    self.f.appendleft(val)
    if len(self.f) > len(self.b) + 1:
      self.b.appendleft(self.f.pop())
      
  def pushMiddle(self, val: int) -> None:
    if len(self.f) == len(self.b):
      self.f.append(val)
    else:
      # len(self.f) == len(self.b) + 1
      self.b.appendleft(self.f.pop())
      self.f.append(val)

  def pushBack(self, val: int) -> None:
    self.b.append(val)
    if len(self.b) > len(self.f):
      self.f.append(self.b.popleft())
    
  def popFront(self) -> int:
    x = -1
    if self.f:
      x = self.f.popleft()
      if len(self.f) < len(self.b):
        self.f.append(self.b.popleft())
    return x
  
  def popMiddle(self) -> int:
    x = -1
    if self.f:
      x = self.f.pop()
      if len(self.f) < len(self.b):
        self.f.append(self.b.popleft())
    return x

  def popBack(self) -> int:
    x = -1
    if self.b:
      x = self.b.pop()
      if len(self.f) > len(self.b) + 1:
        self.b.appendleft(self.f.pop())
    elif self.f:
      x = self.f.pop()
    return x
