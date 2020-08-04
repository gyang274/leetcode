from typing import List

class Solution:
  def fixedPoint(self, A: List[int]) -> int:
    for i, x in enumerate(A):
      if x == i:
        return i
    return -1

class Solution:
  def fixedPoint(self, A: List[int]) -> int:
    # O(logN), binary search, since A in sorted in ascending order
    l, r = 0, len(A) - 1
    while l < r:
      m = l + (r - l) // 2
      if A[m] < m:
        l = m + 1
      else:
        r = m
    return l if A[l] == l else -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [-8,-5,0,3,4,7],
  ]
  rslts = [solver.fixedPoint(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
