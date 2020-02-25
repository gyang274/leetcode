from typing import List

class Solution:
  def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
    """O(N), one pass, keep tracking two words.
    """
    if word1 == word2:
      i0, dist = -len(words), len(words)
      for i, w in enumerate(words):
        if w == word1:
          dist, i0 = min(i - i0, dist), i
    else:
      i1, i2, dist = -len(words), -len(words), len(words)
      for i, w in enumerate(words):
        if w == word1:
          dist, i1 = min(i - i2, dist), i
        if w == word2:
          dist, i2 = min(i - i1, dist), i
    return dist

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"),
    (["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"),
    (["practice", "makes", "perfect", "coding", "makes"], "makes", "makes"),
  ]
  rslts = [solver.shortestWordDistance(words, word1, word2) for words, word1, word2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")