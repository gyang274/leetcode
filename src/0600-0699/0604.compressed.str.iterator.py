class StringIterator:

  def __init__(self, compressedString: str):
    n = len(compressedString)
    self.s = []
    self.c = []
    i = 0
    while i < n:
      self.s.append(compressedString[i])
      i += 1
      j = i
      while j < n and compressedString[j].isdigit():
        j += 1
      self.c.append(int(compressedString[i:j]))
      i = j
    self.i, self.m = 0, len(self.s)
    self.j, self.n = 0, self.c[0] if self.c else 0

  def next(self) -> str:
    x = ' '
    if self.hasNext():
      x = self.s[self.i]
      self.j += 1
      if self.j == self.n:
        self.i += 1
        if self.i < self.m:
          self.j = 0
          self.n = self.c[self.i]
    return x

  def hasNext(self) -> bool:
    return self.i < self.m