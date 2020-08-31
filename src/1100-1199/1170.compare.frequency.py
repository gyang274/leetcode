from typing import List

import bisect

class Solution:
  def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
    def f(s):
      z, n = '\x7f', 0
      for x in s:
        if x < z:
          z, n = x, 0
        if x == z:
          n += 1
      return n
    wc = sorted(map(f, words))
    return [len(wc) - bisect.bisect(wc, x) for x in map(f, queries)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["cbd"], ["zaaaz"]),
    (["bbb","cc"], ["a","aa","aaa","aaaa"]),
  ]
  rslts = [solver.numSmallerByFrequency(queries, words) for queries, words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
