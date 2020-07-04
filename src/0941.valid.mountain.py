from typing import List

class Solution:
  def validMountainArray(self, A: List[int]) -> bool:
    n = len(A)
    if n < 3:
      return False
    i, j = 0, n - 1
    while i < j and A[i] < A[i + 1]:
      i += 1
    while i < j and A[j] < A[j - 1]:
      j -= 1
    return 0 < i == j < n - 1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [2,3,4,1,0],
  ]
  rslts = [solver.validMountainArray(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
