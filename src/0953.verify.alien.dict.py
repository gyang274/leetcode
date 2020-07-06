from typing import List

import string

class Solution:
  def isAlienSorted(self, words: List[str], order: str) -> bool:
    # O(W = sum(len(word)))
    d = {x: y for x, y in zip(order, string.ascii_lowercase)}
    words = list(map(lambda word: ''.join(map(lambda x: d[x], word)), words))
    # O(N)
    n = len(words)
    for i in range(n - 1):
      if words[i] > words[i + 1]:
        return False
    return True
    # O(NlogN)
    # return words == sorted(words)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"),
    (["word","world","row"], "worldabcefghijkmnpqstuvxyz"),
  ]
  rslts = [solver.isAlienSorted(words, order) for words, order in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
