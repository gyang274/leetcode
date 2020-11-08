from typing import List
from collections import defaultdict

class Solution:
  def maxNumOfSubstrings(self, s: str) -> List[str]:
    # TC: O(N), SC: O(1)
    ss = set(s)
    l, r = {x: s.index(x) for x in ss}, {x: s.rindex(x) for x in ss}
    # get valid intervals
    v = []
    for x in ss:
      il, ir = l[x], r[x]
      i = il
      while i <= ir:
        il = min(il, l[s[i]])
        if il < l[x]:
          break
        ir = max(ir, r[s[i]])
        i += 1
      if il == l[x]:
        v.append((il, ir))
    q = [(0, len(s))]
    for i, j in sorted(v):
      if i > q[-1][1]:
        q.append([i, j])
      elif j < q[-1][1]:
        q[-1] = [i, j]
      elif i < q[-1][1]:
        q[-1][1] = j
    return [s[i:(j + 1)] for i, j in q]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "abab",
    "ababa",
    "abbaccd",
    "ceoabcab",
    "adefaddaccc",
  ]
  rslts = [solver.maxNumOfSubstrings(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
