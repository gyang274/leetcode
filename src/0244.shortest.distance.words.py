from typing import List

class WordDistance:
  """O(N^2): double loop to process list once and generate each pairs with shortest distance in hashTable.
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

