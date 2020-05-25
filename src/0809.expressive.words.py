from typing import List

class Solution:
  def runLengthEncode(self, S):
    if S == "":
      return []
    r, x, n = [], S[0], 1
    for s in S[1:] + "#":
      if s == x:
        n += 1
      else:
        r.append((x, n))
        x = s
        n = 1
    return r
  def runLengthDecode(self, word, s):
    if not s:
      return 0 if word else 1
    if not word:
      return 0
    i, y, m = 0, word[0], 1
    for w in word[1:] + "#":
      if w == y:
        m += 1
      else:
        x, n = s[i]
        if x == y and (n == m or n > max(m, 2)):
          y = w
          m = 1
          i += 1
        else:
          return 0
    return 1 if i == len(s) else 0
  def expressiveWords(self, S: str, words: List[str]) -> int:
    s = self.runLengthEncode(S)
    return sum(self.runLengthDecode(word, s) for word in words)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("ab", ["abb"]),
    ("abcd" , ["abc"]),
    ("heeellooo", ["hello", "hi", "helo"]),
  ]
  rslts = [solver.expressiveWords(S, words) for S, words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
