import string
import operator

from itertools import starmap

class Solution:
  def minimumDistance(self, word: str) -> int:
    # hash: character to coordinates
    hash = {s: ((ord(s) - ord('A')) // 6, (ord(s) - ord('A')) % 6) for s in string.ascii_uppercase}
    # dist: L1 distacne between characters
    dist = lambda s, t: sum(abs(hs - ht) for hs, ht in zip(hash[s], hash[t]))
    # dp
    # dp[i][j] is the min distance of typing i-th character with the other finger at j-th character, j in [0, 25]
    x = [0] * 26
    for i in range(1, len(word)):
      # move from word[i-1] to word[i], the other finger still on j-th character.
      y = list(starmap(operator.__add__, zip(x, [dist(word[i - 1], word[i])] * 26)))
      # move from j-th character to word[i], the other finger is on the word[i-1].
      k = ord(word[i - 1]) - ord('A')
      for j in range(26):
        y[k] = min(y[k], x[j] + dist(string.ascii_uppercase[j], word[i]))
      x = y
    return min(x)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "LEETCODE",
  ]
  rslts = [solver.minimumDistance(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
