class DSU:
  def __init__(self, reps: dict = {}):
    # representer
    self.reps = reps
  def add(self, x):
    self.reps[x] = x
  def find(self, x):
    while not x == self.reps[x]:
      x = self.reps[x]
    return x
  def union(self, x, y):
    self.reps[self.find(y)] = self.find(x)

class DSU:
  def __init__(self):
    # representer
    self.reps = {}
    self.size = {}
  def add(self, x):
    self.reps[x] = x
    self.size[x] = 1
  def find(self, x):
    while not x == self.reps[x]:
      x = self.reps[x]
    return x
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
