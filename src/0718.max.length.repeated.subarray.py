from typing import List

class Solution:
  def findLength(self, A: List[int], B: List[int]) -> int:
    m, n = len(A), len(B)
    xmax = 0
    for i in range(m):
      for j in range(n):
        if A[i] == B[j] and (i == 0 or j == 0 or not A[i - 1] == B[j - 1]):
          k = 1
          while i + k < m and j + k < n and A[i + k] == B[j + k]:
            k += 1
          xmax = max(k, xmax)
    return xmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], [3,2,1,1,4]),
  ]
  rslts = [solver.findLength(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
