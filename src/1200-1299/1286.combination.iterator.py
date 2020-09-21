class CombinationIterator:

  def __init__(self, characters: str, combinationLength: int):
    self.s = characters
    self.n = len(characters)
    self.k = combinationLength
    self.x = list(range(self.k - 1, -1, -1))
    self.i = 0

  def next(self) -> str:
    s = ''.join(self.s[i] for i in self.x[::-1])
    while self.i < self.k and self.x[self.i] + 1 == self.n - self.i:
      self.i += 1
    if self.i < self.k:
      self.x[self.i] += 1
      for i in range(self.i, -1, -1):
        self.x[i] = self.x[self.i] + self.i - i
      self.i = 0
    return s

  def hasNext(self) -> bool:
    return self.i < self.k