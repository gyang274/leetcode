from typing import List

import re

class Solution:
  def findWords(self, words: List[str]) -> List[str]:
    # keyboard line
    KLlist = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]
    KLdict = {}
    for i, s in enumerate(KLlist):
      for x in s:
        KLdict[x] = i
    # hash word to keyboard line
    ans = []
    for word in words:
      ok, kl = True, None
      for x in word:
        if kl is None:
          kl = KLdict[x]
        elif kl == KLdict[x]:
          continue
        else:
          ok = False
          break
      if ok:
        ans.append(word)
    return ans

class Solution:
  def findWords(self, words: List[str]) -> List[str]:
    return list(filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words))

class Solution:
  def findWords(self, words: List[str]) -> List[str]:
    kl0, kl1, kl2 = set("qwertyuiop"), set("asdfhjkl"), set("zxcvbnm")
    ans = []
    for word in words:
      ws = set(word.lower())
      if ws <= kl0 or ws <= kl1 or ws <= kl2:
        ans.append(word)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["Hello", "World", "Alaska", "DasKL", "Peace", "AA", "Qq", "Zz"],
  ]
  rslts = [solver.findWords(words) for words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  