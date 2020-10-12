from typing import List
from collections import Counter

class Solution:
  def findLucky(self, arr: List[int]) -> int:
    d = Counter(arr)
    for x in sorted(d.keys(), reverse=True):
      if d[x] == x:
        return x
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [2,2,3,3,3],
  ]
  rslts = [solver.findLucky(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
