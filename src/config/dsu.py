class DSU:
  def __init__(self, reps: dict = {}):
    # representer
    self.reps = reps
  def add(self, x):
    self.reps[x] = x
  def find(self, x):
    if not x == self.reps[x]:
      self.reps[x] = self.find(self.reps[x])
    return self.reps[x]
  def union(self, x, y):
    self.reps[self.find(y)] = self.find(x)

class DSU:
  def __init__(self):
    self.reps = {}
    self.size = {}
  def add(self, x):
    self.reps[x] = x
    self.size[x] = 1
  def find(self, x):
    if not x == self.reps[x]:
      self.reps[x] = self.find(self.reps[x])
    return self.reps[x]
  def union(self, x, y):
    hX = self.find(x)
    hY = self.find(y)
    if not hX == hY:
      h = min(hX, hY)
      if h == hX:
        self.reps[hY] = h
        self.size[hX] += self.size[hY]
        self.size.pop(hY)
      else:
        self.reps[hX] = h
        self.size[hY] += self.size[hX]
        self.size.pop(hX)

class DSU:
  def __init__(self):
    self.reps = {}
    self.rank = {}
  def add(self, x):
    self.reps[x] = x
    self.rank[x] = 0
  def find(self, x):
    # path compression
    if not x == self.reps[x]:
      self.reps[x] = self.find(self.reps[x])
    return self.reps[x]
  def union(self, x, y):
    # union by rank
    hX = self.find(x)
    hY = self.find(y)
    if not hX == hY:
      h = hY if self.rank[hX] < self.rank[hY] else hX
      if self.rank[hX] == self.rank[hY]:
        self.rank[h] += 1
      self.reps[hX] = h
      self.reps[hY] = h
