from typing import List
from collections import Counter
from functools import reduce

import operator

class Solution:
  def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
    # Key: O(WP) => O(W + 64P)
    # since len(puzzle) == 7 for each puzzle, so total possible hash <= 2^6
    # - counter of words hashs
    counter = Counter(map(lambda word: reduce(operator.__or__, map(lambda x: 1 << (ord(x) - ord('a')), word)) , words))
    # - sum over each possible hash (max 64 of such hash) for each puzzle
    ans = [0] * len(puzzles)
    for i, p in enumerate(puzzles):
      phash = {1 << (ord(p[0]) - ord('a'))}
      for x in p[1:]:
        phash |= {(z | (1 << (ord(x) - ord('a')))) for z in phash}
      for h in phash:
        ans[i] += counter[h]
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["aaaa","asas","able","ability","actt","actor","access"], ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]),
  ]
  rslts = [solver.findNumOfValidWords(words, puzzles) for words, puzzles in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
