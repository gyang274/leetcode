from typing import List
from collections import defaultdict

class Solution:
  def recursive(self, indices, k):
    # seens: hashmap (prefix, length, suffix) -> index
    seens = defaultdict(list)
    for i in indices:
      if k > len(self.words[i]) - 3:
        self.abbrs[i] = self.words[i]
      else:
        seens[(self.words[i][:k], len(self.words[i]), self.words[i][-1])].append(i)
    # create abbreviation for all collisional words together
    for _, v in seens.items():
      if len(v) == 1:
        self.abbrs[v[0]] = self.words[v[0]][:k] + str(len(self.words[v[0]]) - k - 1) + self.words[v[0]][-1]
      else:
        self.recursive(v, k + 1)
  def wordsAbbreviation(self, words: List[str]) -> List[str]:
    self.abbrs, self.words = [None] * len(words), words
    self.recursive([i for i in range(len(words))], 1)
    return self.abbrs

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"],
  ]
  rslts = [solver.wordsAbbreviation(words) for words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
