from typing import List
from collections import defaultdict

class ValidWordAbbr:
  def __init__(self, dictionary: List[str]):
    self.words = set([])
    self.abbrs = defaultdict(lambda: 0)
    for word in dictionary:
      if word not in self.words:
        self.words.add(word)
        self.abbrs[self._word2abbr(word)] += 1
  def _word2abbr(self, word):
    return word if len(word) < 2 else (word[0] + str(len(word) - 2) + word[-1])
  def isUnique(self, word: str) -> bool:
    abbr = self._word2abbr(word)
    if word not in self.words:
      return self.abbrs[abbr] < 1
    else:
      return self.abbrs[abbr] < 2
      