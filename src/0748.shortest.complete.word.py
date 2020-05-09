from typing import List
from collections import Counter

class Solution:
  def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
    words = sorted([(len(word), index, word) for index, word in enumerate(words)])
    plate = ""
    for w in licensePlate:
      if w.isalpha():
        plate += w.lower()
    cntr = Counter(plate)
    for _, i, word in words:
      if cntr == cntr & Counter(word):
        return word
    return None
        