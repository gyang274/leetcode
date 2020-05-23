from typing import List

import string

class Solution:
  def numMatchingSubseq(self, S: str, words: List[str]) -> int:
    """O(26|S| preprocessing + \sum_i|W_i| comparison)
    """
    n = len(S)
    # preprocessing O(26N)
    # d[i + 1][j]: S[i] next see jth character in a-z at index d[i + 1][j]
    dp = [[-1] * 26 for _ in range(n + 1)]
    for j, x in enumerate(string.ascii_lowercase):
      nuxt = -1
      for i in range(n - 1, -1, -1):
        dp[i + 1][j] = nuxt
        if S[i] == x:
          nuxt = i + 1
      dp[0][j] = nuxt
    # each words issubset is O(|W|)
    count = len(words)
    for word in words:
      i, n = 0, len(word)
      for j, w in enumerate(word):
        i = dp[i][ord(w) - ord('a')]
        if i == -1:
          count -= 1
          break
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abcde", ["a","bb","acd","ace"]),
  ]
  rslts = [solver.numMatchingSubseq(S, words) for S, words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
