class Vector2D:
  def __init__(self, v: List[List[int]]):
    self.v = v
    # i, j traversal in 1st and 2nd level respectively, move j if possible otherwise i.
    self.i = 0
    self.j = 0
    # init i, j into 1st valid index pair, in case of [[], ..] empty list item in list of list
    while self.i < len(self.v) and not self.v[self.i]:
      self.i += 1
  def next(self) -> int:
    x = self.v[self.i][self.j]
    if self.j + 1 < len(self.v[self.i]):
      self.j += 1
    else:
      self.i += 1
      # in case of [[], ..] empty list item in list of list
      while self.i < len(self.v) and not self.v[self.i]:
        self.i += 1
      self.j = 0
    return x
  def hasNext(self) -> bool:
    return self.i < len(self.v) # and self.j < len(self.v[self.i])