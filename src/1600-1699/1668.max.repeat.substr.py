class Solution:
  def maxRepeating(self, sequence: str, word: str) -> int:
    # rolling hash, TC: O(N), SC: O(N) or O(M) or O(1)?
    n, m = len(sequence), len(word)
    if n < m:
      return 0
    # hash of word
    h = 0
    for x in word:
      h = h * 26 + (ord(x) - ord('a'))
    # rolling hash
    k = [0] * n
    r, s = 0, sequence
    for i in range(m):
      r = r * 26 + (ord(s[i]) - ord('a'))
    if r == h:
      k[m - 1] = 1
    M = 26 ** m
    for i in range(m, n):
      r = r * 26 + (ord(s[i]) - ord('a')) - (ord(s[i - m]) - ord('a')) * M
      if r == h:
        k[i] += k[i - m] + 1
    return max(k)
