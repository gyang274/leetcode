from typing import List

import itertools

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

class Solution:
  def numSimilarGroups(self, A: List[str]) -> int:
    """TC: O(NWmin(N,W^2)), min of O(N^2W) pairwise similar and O(NW W^2) generate all similar in a set.
    """
    n, w = len(A), len(A[0])
    # branch
    if n < w * w:
      # disjoint set union
      dsu = DSU(reps={i:i for i in range(n)})
      # pairwise similar O(N^2 W)
      # simiar O(W): determine similarity between words
      similar = lambda word1, word2: sum(x != y for x, y in zip(word1, word2)) < 3
      # pairwise O(N^2): determine similarity between each pair
      for (i1, word1), (i2, word2) in itertools.combinations(enumerate(A), 2):
        if similar(word1, word2):
          dsu.union(i1, i2)
      count = sum(dsu.reps[i] == i for i in range(n))
    else:
      # generate all candidates
      words, count = set(A), 0
      while words:
        stack = [words.pop()]
        while stack:
          word = list(stack.pop())
          for i0, i1 in itertools.combinations(range(w), 2):
            word[i0], word[i1] = word[i1], word[i0]
            wnxt = ''.join(word)
            if wnxt in words:
              stack.append(wnxt)
              words.remove(wnxt)
            word[i0], word[i1] = word[i1], word[i0]
        count += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["tars","arts","star"],
    ["tars","rats","arts","star"],
  ]
  rslts = [solver.numSimilarGroups(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")