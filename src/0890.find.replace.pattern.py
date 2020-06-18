from typing import List

class Solution:
  def samePattern(self, word: str, pattern: str) -> str:
    d, p = {}, {}
    for x, y in zip(word, pattern):
      if x not in d and y not in p:
        d[x] = y
        p[y] = x
      elif not (x in d and y in p and d[x] == y and p[y] == x):
        return False
    return True
  def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
    return [word for word in words if self.samePattern(word, pattern)]

class Solution:
  def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
    def match(word):
      d, p = {}, {}
      for x, y in zip(word, pattern):
        if x not in d:
          d[x] = y
        if y not in p:
          p[y] = x
        if (d[x], p[y]) != (y, x):
          return False
      return True
    return list(filter(match, words))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["abc","deq","mee","aqq","dkd","ccc"], "abb"),
  ]
  rslts = [solver.findAndReplacePattern(words, pattern) for words, pattern in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
