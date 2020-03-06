from typing import List
from collections import defaultdict

class Solution:
  def _wordBitmask(self, word):
    bitmask = 0
    for w in word:
      bitmask |= 1 << (ord(w) - ord('a'))
    return bitmask
  def maxProduct(self, words: List[str]) -> int:
    """preprocessing + bitmask + hashmap.
      preprocessing: map each word to bitmask 0/1 on index 0-25 to represent a character exist or not.
      bitmask: bitmask & operation to determine two words overlap any character or not.
      hashmap: words mapping to same bitmask (words with same set of characters) need only keep the longest one.
    """
    # wdict: key by bitmask, value is the length of longest word mapping to this bitmask.
    wdict = defaultdict(lambda: 0)
    for word in words:
      bitmask = self._wordBitmask(word)
      wdict[bitmask] = max(wdict[bitmask], len(word))
    # double loop over wdict?
    xmax = 0
    for b1 in wdict:
      for b2 in wdict:
        if b1 & b2 == 0:
          xmax = max(xmax, wdict[b1] * wdict[b2])
    return xmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["a","aa","aaa","aaaa"],
    ["a","ab","aba","abab", "cd"],
    ["a","ab","abc","d","cd","bcd","abcd"],
    ["abcw","baz","foo","bar","xtfn","abcdef"],
  ]
  rslts = [solver.maxProduct(words) for words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
        