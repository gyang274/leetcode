from typing import List
from collections import Counter
from itertools import starmap

import operator

class Solution:
  def countCharacters(self, words: List[str], chars: str) -> int:
    xc = Counter(chars)
    # ok: can word be formed by characters?
    ok = lambda wc: all(xc[x] >= wc[x] for x in wc)
    return sum(starmap(operator.__mul__, zip(map(len, words), map(ok, map(Counter, words)))))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["cat","bt","hat","tree"], "atach"),
    (["hello","world","leetcode"], "welldonehoneyr"),
  ]
  rslts = [solver.countCharacters(words, chars) for words, chars in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")