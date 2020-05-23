from typing import List, Dict

class DSU:
  def __init__(self, reps: Dict = {}):
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

class Solution:
  def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
    """disjoint union set
    """
    if not len(words1) == len(words2):
      return False
    dsu = DSU(reps={})
    for w1, w2 in pairs:
      if w1 not in dsu.reps:
        dsu.add(w1)
      if w2 not in dsu.reps:
        dsu.add(w2)
      dsu.union(w1, w2)
    for w1, w2 in zip(words1, words2):
      if not (w1 == w2 or (w1 in dsu.reps and w2 in dsu.reps and dsu.find(w1) == dsu.find(w2))):
        return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["great","acting","skills"], ["fine","drama","talent"], [["great","fine"],["drama","acting"],["skills","talent"]]),
    (["great","acting","skills"], ["fine","drama","talent"], [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]),
  ]
  rslts = [solver.areSentencesSimilarTwo(words1, words2, pairs) for words1, words2, pairs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")