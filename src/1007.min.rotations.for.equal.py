from typing import List
from collections import Counter

class Solution:
  def minDominoRotations(self, A: List[int], B: List[int]) -> int:
    n, d = len(A), Counter(A + B).most_common()[0]
    if d[1] < n:
      return -1
    x, fA, fB = d[0], 0, 0
    for i in range(n):
      if A[i] == x and B[i] == x:
        continue
      elif A[i] == x:
        fB += 1
      elif B[i] == x:
        fA += 1
      else:
        return -1
    return min(fA, fB)

class Solution:
  def minDominoRotations(self, A: List[int], B: List[int]) -> int:
    for x in [A[0],B[0]]:
      if all(x in d for d in zip(A, B)):
        return len(A) - max(A.count(x), B.count(x))
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([3,5,1,2,3], [3,6,3,3,4]),
    ([2,1,2,4,2,2], [5,2,6,2,3,2]),
  ]
  rslts = [solver.minDominoRotations(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
