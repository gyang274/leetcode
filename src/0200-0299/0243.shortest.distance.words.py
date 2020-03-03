from typing import List

class Solution:
  def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
    """O(N), one pass, keep tracking two words.
    """
    i1, i2, dist = -1, -1, len(words)
    for i, w in enumerate(words):
      if w == word1:
        i1 = i
        dist = min((i1 - i2), dist) if not i2 == -1 else len(words)
      if w == word2:
        i2 = i
        dist = min((i2 - i1), dist) if not i1 == -1 else len(words)
    return dist

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"),
    (["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"),
  ]
  rslts = [solver.shortestDistance(words, word1, word2) for words, word1, word2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
        