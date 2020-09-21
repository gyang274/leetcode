from typing import List
from collections import Counter
from functools import reduce

import operator

class Solution:
  def recursive(self, words, counter, score):
    self.ms = max(self.ms, score)
    # wc: word-character-counter, ws: word-score
    for i, (wc, ws) in enumerate(words):
      if all(counter[x] >= wc[x] for x in wc):
        # NOTE: no words[:i] as skipped, no duplicates
        # self.recursive(words[:i] + words[(i + 1):], counter - wc, score + ws)
        self.recursive(words[(i + 1):], counter - wc, score + ws)
    return None
  def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
    self.ms = 0
    # words: list of (word-character-counter, word-score)
    words = list(map(
      lambda word: (Counter(word), reduce(operator.__add__, map(lambda x: score[ord(x)-ord('a')], word))), words
    ))
    # counter of letters
    counter = Counter(letters)
    # dfs with backtrack
    self.recursive(words, counter, 0)
    return self.ms

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]),
    (["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]),
    (["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]),
    (
      ["daeagfh","acchggghfg","feggd","fhdch","dbgadcchfg","b","db","fgchfe","baaedddc"],
      [
        "a","a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","d",
        "d","d","d","d","d","d","d","d","d","d","d","d","d","e","e","e","e","e","e","e","e","e","e","f","f","f","f","f",
        "f","f","f","f","f","f","f","f","f","g","g","g","g","g","g","g","g","g","g","g","g","h","h","h","h","h","h","h",
        "h","h","h","h","h","h"
      ],
      [2,1,9,2,10,5,7,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ),
  ]
  rslts = [solver.maxScoreWords(words, letters, score) for words, letters, score in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
