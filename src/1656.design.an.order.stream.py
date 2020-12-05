from collections import deque

class OrderedStream:

  def __init__(self, n: int):
    self.L = deque([None] * n)
    # self.p: pointer to next empty slot
    self.p = 1
        
  def insert(self, id: int, value: str) -> List[str]:
    # insert
    self.L[id - self.p] = value
    x = []
    while self.L and self.L[0]:
      x.append(self.L.popleft())
      self.p += 1
    return x
