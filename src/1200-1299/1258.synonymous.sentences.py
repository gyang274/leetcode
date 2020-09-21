from typing import List
from collections import defaultdict
from itertools import product

class DSU:
  def __init__(self, reps):
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

class Solution:
  def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
    # dsu
    dsu = DSU(reps = {})
    for x, y in synonyms:
      if x not in dsu.reps:
        dsu.add(x)
      if y not in dsu.reps:
        dsu.add(y)
      dsu.union(x, y)
    # d: h -> all-synonyms
    d = defaultdict(set)
    for x in dsu.reps:
      d[dsu.find(x)].add(x)
    # all sentences
    return sorted([' '.join(s) for s in product(*[[x] if x not in dsu.reps else d[dsu.find(x)] for x in text.split()])])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([["happy","joy"],["sad","sorrow"],["joy","cheerful"]], "I am happy today but was sad yesterday"),
  ]
  rslts = [solver.generateSentences(synonyms, text) for synonyms, text in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
