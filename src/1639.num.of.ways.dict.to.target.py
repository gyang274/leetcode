from typing import List

from functools import lru_cache

class Solution:
  def __init__(self):
    self.M = 10 ** 9 + 7
  @lru_cache(None)
  def match(self, i, j):
    # num of ways when match s[i] <-> t[j]
    m = self.s[i][self.t[j]]
    if m == 0:
      return 0
    if j + 1 == len(self.t):
      return m   
    ans = 0
    for k in range(i + 1, len(self.s) - (len(self.t) - (j + 1)) + 1):
      ans += m * self.match(k, j + 1)
    return ans % self.M
  def numWays(self, words: List[str], target: str) -> int:
    self.match.cache_clear()
    # s
    self.s = [[0] * 26 for _ in range(len(words[0]))]
    for word in words:
      for i, x in enumerate(word):
        self.s[i][ord(x) - ord('a')] += 1
    # t
    self.t = [ord(y) - ord('a') for y in target]
    # count
    count = 0
    for i in range(len(self.s) - len(self.t) + 1):
      count = (count + self.match(i, 0)) % self.M
    return count % self.M

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["abab","baba","abba","baab"], "abba"),
    (["ababab","bababa","ababab","abaaba"], "abba"),
  ]
  rslts = [solver.numWays(words, target) for words, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")

