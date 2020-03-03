from typing import List
from collections import defaultdict

class WordDistance:
  """init: TC O(N^2), SC O(N^2) + search: O(1)
    At __init__, double loop to process words list once and generate each pairs with shortest distance in hashTable.
    For each word already seen, loop back half way to previous seen index and update shortest distance in hashTable.
  """
  def __init__(self, words: List[str]):
    self.words = words
    # self.dists: hash each word to its last index, and hash each words pair to their shortest distance.
    self.dists = {}
    for i2, w2 in enumerate(self.words):
      i1_left = -1 if w2 not in self.dists else (self.dists[w2] + (i2 - self.dists[w2]) // 2)
      self.dists[w2] = i2
      for i1 in range(i2 - 1, i1_left, -1):
        w1 = self.words[i1]
        # calcuate the dist
        if (w1, w2) not in self.dists:
          dist = i2 - self.dists[w1]
        else:
          dist = min(i2 - self.dists[w1], self.dists[(w1, w2)])
        # update the dist on both side
        self.dists[(w1, w2)] = dist
        self.dists[(w2, w1)] = dist
  def shortest(self, word1: str, word2: str) -> int:
    return self.dists[(word1, word2)]

class WordDistance:
  """init: TC O(N), SC O(N) + search O(k)
    At __init__, process and maintain a hashTable of word -> indices. At search go through word1 word2 index in order.
  """
  def __init__(self, words: List[str]):
    self.windex = defaultdict(list)
    for i, w in enumerate(words):
      self.windex[w].append(i)
    self.maxdist = len(words)
  def shortest(self, word1: str, word2: str) -> int:
    w1idx, w2idx = self.windex[word1], self.windex[word2]
    # w1 ende earlier
    if w1idx[-1] > w2idx[-1]:
      w1idx, w2idx = w2idx, w1idx
    # # special case, in case word1 appears all the time 0, ..., 99999 and word2 appears once at 100000
    # if w1idx[-1] < w2idx[0]:
    #   return w2idx[0] - w1idx[-1]
    # wdlast: last seen is word1 or word2?
    i1, i2, dist, idlast, wdlast = 0, 0, self.maxdist, -self.maxdist, 0
    while True:
      if i1 < len(w1idx) and w1idx[i1] < w2idx[i2]:
        # this is w1, last is w1 or w2?
        if wdlast == 2:
          dist = min(w1idx[i1] - idlast, dist)
        idlast = w1idx[i1]
        wdlast = 1
        i1 += 1
      else:
        # this is w2, last is w1 or w2?
        if wdlast == 1:
          dist = min(w2idx[i2] - idlast, dist)
        idlast = w2idx[i2]
        wdlast = 2
        i2 += 1
        # ealry break, in case: word1 appears once at 0, word2 appears all other 1, ..., 100000
        # note: keep this in `else` so that the i2 += 1 make sure i2 > 0 in w2idx[i2 - 1] > w1idx[i1]
        if i2 == len(w2idx) or (i1 == len(w1idx) and w2idx[i2 - 1] > w1idx[i1 - 1]):
          break
    return dist

class WordDistance:
  def __init__(self, words: List[str]):
    self.windex = defaultdict(list)
    for i, w in enumerate(words):
      self.windex[w].append(i)
    self.maxdist = len(words)
  def shortest(self, word1, word2):
    w1idx, w2idx = self.windex[word1], self.windex[word2]
    i1, i2, dist = 0, 0, self.maxdist
    while i1 < len(w1idx) and i2 < len(w2idx):
      dist = min(abs(w1idx[i1] - w2idx[i2]), dist)
      if w1idx[i1] < w2idx[i2]:
        i1 += 1
      else:
        i2 += 1
    return dist

if __name__ == '__main__':
  # case1
  solver = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
  cases = [
    ("makes", "coding"),
    ("coding", "practice"),
  ]
  rslts = [solver.shortest(word1, word2) for word1, word2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
  # case2
  solver = WordDistance([
    "this","is","a","long","run","sentence","is","fun","day","today","sunny","weather","is","a","day","tuesday",
    "this","sentence","running","rainy",
  ])
  cases = [
    ("this","is"),
    ("sentence","a"),
    ("is","a"),
    ("this","sentence"),
    ("weather","long"),
    ("day","sentence"),
    ("rainy","tuesday"),
    ("this","rainy"),
    ("running","run"),
  ]
  rslts = [solver.shortest(word1, word2) for word1, word2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")