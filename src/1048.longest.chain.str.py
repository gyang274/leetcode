from typing import List
from itertools import groupby

class Solution:
  def chainOk(self, word1, word2):
    m, n = len(word1), len(word2)
    if not m == n - 1:
      return False
    i, j, k = 0, 0, 0
    while i < m:
      if word1[i] == word2[j]:
        i += 1
        j += 1
      elif not k:
        j += 1
        k += 1
      else:
        return False
    return True
  def longestStrChain(self, words: List[str]) -> int:
    # w1 <- w2, necessary condition: len(w1) = len(w2) - 1
    words.sort(key=len)
    # group words into sublist of words with same length
    # ws: [(length, [(index, word), ..]), ..]
    ws = [(k, list(v)) for k, v in groupby(enumerate(words), lambda x: len(x[1]))]
    # O(N^2W)
    m, n = len(ws), len(words) 
    chain = [1] * n
    for l in range(1, m):
      if ws[l - 1][0] == ws[l][0] - 1:
        for i1, w1 in ws[l - 1][1]:
          for i2, w2 in ws[l][1]:
            if self.chainOk(w1, w2):
              chain[i2] = max(chain[i2], chain[i1] + 1)
    return max(chain)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["a","b","ab","abc","abd","abcd","abcde", "abccde"],
  ]
  rslts = [solver.longestStrChain(words) for words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
