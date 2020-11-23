from typing import List

import string

class Solution:
  def modifyString(self, s: str) -> str:
    ans, n = list(s), len(s)
    for i, x in enumerate(ans):
      if x == '?':
        y = set(string.ascii_lowercase)
        if i - 1 >= 0:
          y -= set(ans[i - 1])
        if i + 1 < n:
          y -= set(ans[i + 1])
        ans[i] = y.pop()
    return ''.join(ans)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "a?zs",
  ]
  rslts = [solver.modifyString(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
