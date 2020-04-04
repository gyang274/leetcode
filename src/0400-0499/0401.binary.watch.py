from typing import List
from collections import defaultdict

class Solution:
  def __init__(self):
    self.hh = defaultdict(list)
    self.mm = defaultdict(list)
    for h in range(12):
      k = bin(h)[2:].count("1")
      self.hh[k].append(str(h))
    for m in range(60):
      k = bin(m)[2:].count("1")
      self.mm[k].append(str(m).zfill(2))
  def readBinaryWatch(self, num: int) -> List[str]:
    ans = []
    for nh in range(min(num + 1, 4)):
      for h in self.hh[nh]:
        for m in self.mm[num - nh]:
          ans.append(h + ":" + m)
    return ans 

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 2, 3, 5, 8,
  ]
  rslts = [solver.readBinaryWatch(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")