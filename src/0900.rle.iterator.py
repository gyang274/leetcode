from itertools import accumulate

class RLEIterator:

  def __init__(self, A: List[int]):
    self.r, self.x = list(accumulate(A[::2])), A[1::2]
    self.i, self.n, self.count = 0, len(A) // 2, 0
  
  def next(self, n: int) -> int:
    self.count += n
    while self.i < self.n and self.count > self.r[self.i]:
      self.i += 1
    return self.x[self.i] if self.i < self.n else -1
