from typing import List

class Solution:
  def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    m, n = len(A), len(B)
    i, j, ans = 0, 0, []
    while i < m and j < n:
      while j < n and B[j][1] < A[i][0]:
        j += 1
      while j < n and B[j][1] <= A[i][1]:
        ans.append([max(A[i][0], B[j][0]), B[j][1]])
        j += 1
      if j < n and B[j][0] <= A[i][1]:
        ans.append([max(A[i][0], B[j][0]), A[i][1]])
      i += 1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]),
  ]
  rslts = [solver.intervalIntersection(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
