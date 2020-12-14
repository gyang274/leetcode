import string

class DSU:
  def __init__(self, reps: dict = {}):
    self.reps = reps
  def find(self, x):
    if not x == self.reps[x]:
      self.reps[x] = self.find(self.reps[x])
    return self.reps[x]
  def union(self, x, y):
    rX = self.find(x)
    rY = self.find(y)
    self.reps[rX] = self.reps[rY] = min(rX, rY)

class Solution:
  def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
    # disjoint set union
    dsu = DSU(reps = {x: x for x in string.ascii_lowercase})
    # dsu with smallest character as representer
    for x, y in zip(A, B):
      dsu.union(x, y)
    return ''.join(map(lambda x: dsu.find(x), S))
    
if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("hello", "world", "hold"),
    ("parker", "morris", "parser"),
    ("leetcode", "programs", "sourcecode"),
  ]
  rslts = [solver.smallestEquivalentString(A, B, S) for A, B, S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
