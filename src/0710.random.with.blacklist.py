import random

class Solution:
  def __init__(self, N: int, blacklist: List[int]):
    self.n = N - len(blacklist)
    self.d = {}
    k, b = 0, set(blacklist)
    for v in sorted(blacklist):
      if v < self.n:
        while self.n + k in b:
          k += 1
        self.d[v] = self.n + k
        k += 1
  def pick(self) -> int:
    v = random.randrange(self.n)
    return self.d[v] if v in self.d else v
