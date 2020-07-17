from typing import List
from itertools import accumulate

class Solution:
  def partitionDisjoint(self, A: List[int]) -> int:
    l, r = list(accumulate(A, max)), list(reversed(list(accumulate(reversed(A), min))))
    for i, x in enumerate(l):
      if x <= r[i + 1]:
        return i + 1
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
    [1,0,1,1,2,3],
    [1,1,1,0,2,3],
    [29,33,6,4,42,0,10,22,62,16,46,75,100,67,70,74,87,69,73,88]
  ]
  rslts = [solver.partitionDisjoint(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
