from typing import List
from collections import Counter

class Solution:
  def countElements(self, arr: List[int]) -> int:
    d = Counter(arr)
    return sum(d[k] for k in d if k + 1 in d)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.countElements(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
