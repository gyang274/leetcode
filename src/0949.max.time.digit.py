from typing import List
from itertools import permutations

class Solution:
  def largestTimeFromDigits(self, A: List[int]) -> str:
    f = list(filter(lambda x: x[0] * 10 + x[1] < 24 and x[2] * 10 + x[3] < 60, permutations(A)))
    if not f:
      return ''
    x = max(f)
    return str(x[0]) + str(x[1]) + ':' + str(x[2]) + str(x[3])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0,0,0,0],
    [2,3,1,4],
    [2,0,4,8],
    [5,5,5,5],
  ]
  rslts = [solver.largestTimeFromDigits(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
