from collections import defaultdict

import heapq

class FreqStack:
  # hash + priority queue
  def __init__(self):
    self.d = defaultdict(lambda: 0)
    self.q = []
    self.i = 0
  def push(self, x: int) -> None:
    self.i += 1
    self.d[x] += 1
    heapq.heappush(self.q, (-self.d[x], -self.i, x))
  def pop(self) -> int:
    _, _, x = heapq.heappop(self.q)
    self.d[x] -= 1
    return x
  
class FreqStack:
  # stack of stacks
  def __init__(self):
    self.d = defaultdict(lambda: 0)
    self.q = defaultdict(list)
    self.m = 0
  def push(self, x: int) -> None:
    self.d[x] += 1
    if self.d[x] > self.m:
      self.m = self.d[x]
    self.q[self.d[x]].append(x)
  def pop(self) -> int:
    x = self.q[self.m].pop()
    self.d[x] -= 1
    if not self.q[self.m]:
      self.m -= 1
    return x