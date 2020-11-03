from typing import List
from collections import defaultdict

class Solution:
  def getFolderNames(self, names: List[str]) -> List[str]:
    d, ans = {}, []
    for x in names:
      if x in d:
        i = d[x]
        while f"{x}({i})" in d:
          i += 1
        d[x] = i + 1
        d[f"{x}({i})"] = 1
        ans.append(f"{x}({i})")
      else:
        d[x] = 1
        ans.append(x)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["fifa","fifa(2002)","pes","pes(2019)"],
    ["avalon","avalon","avalon","avalon","avalon"],
    ["avalon","avalon","avalon","avalon(1)","avalon(1)"],
    ["avalon","avalon","avalon","avalon(2)","avalon(3)"],
    ["avalon","avalon(1)","avalon","avalon(1)","avalon","avalon(1)"],
  ]
  rslts = [solver.getFolderNames(names) for names in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
