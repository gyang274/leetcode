from typing import List
from collections import defaultdict

class Solution:
  def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
    d = defaultdict(set)
    for p, pp in zip(pid, ppid):
      d[pp].add(p)
    queue, s = set([kill]), set([])
    while queue:
      bound = set([])
      for pp in queue:
        s.add(pp)
        if pp in d:
          bound |= d[pp]
      queue = bound
    return s

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,3,10,5], [3,0,5,3], 5),
  ]
  rslts = [solver.killProcess(pid, ppid, kill) for pid, ppid, kill in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
