from typing import List
from collections import defaultdict
from itertools import chain

class Solution:
  def generatePermutation(self, rslt, xlist):
    if len(xlist) == 0:
      self.ans.append(rslt)
    elif len(xlist) == 1:
      self.ans.append(rslt + xlist[0])
    else:
      for i in range(len(xlist)):
        if i == 0 or not xlist[i] == xlist[i - 1]:
          self.generatePermutation(rslt + xlist[i], xlist[:i] + xlist[(i + 1):])
  def generatePalindromes(self, s: str) -> List[str]:
    """At most one character showed odd number of times, get half of palindrome + `middle` + reverse.
    """
    xdict = defaultdict(lambda: 0)
    for x in s:
      xdict[x] += 1
    xmiddle = ""
    for x in xdict:
      # x % 2 == 1
      if xdict[x] & (-xdict[x]) == 1:
        if not xmiddle == "":
          return []
        xmiddle = x
        # if xdict[x] == 1:
        #   xdict.pop(x)
        xdict[x] -= 1
      # xdict[x] //= 2
      xdict[x] >>= 1
    # xlist of characters (characters with repeat, same character adjancet to each other) in 1st half
    xlist = list(chain.from_iterable([x] * xdict[x] for x in xdict))
    self.ans = []
    self.generatePermutation("", xlist)
    return [x + xmiddle + x[::-1] for x in self.ans]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "", "a", "ab", "aab", "aabb", "aaabb", "carerec",
  ]
  rslts = [solver.generatePalindromes(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")