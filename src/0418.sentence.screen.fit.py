from typing import List

class Solution:
  def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
    # build an mapping of row start word index -> ende word index along the way
    i, n, se = 0, 0, {}
    for r in range(rows):
      if i not in se:
        k, l, m = i, 0, 0
        while l < cols:
          l += len(sentence[k]) + 1
          if l <= cols + 1:
            k += 1
            if k == len(sentence):
              m += 1
              k  = 0
        se[i] = [k, m]
      i, n = se[i][0], n + se[i][1]
    return n

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["a", "b"], 3, 6),
    (["a", "bcd", "e"], 3, 6),
    (["hello", "word"], 2, 8),
  ]
  rslts = [solver.wordsTyping(sentence, rows, cols) for sentence, rows, cols in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
        