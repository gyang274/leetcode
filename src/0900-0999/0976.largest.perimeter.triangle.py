from typing import List

class Solution:
  def largestPerimeter(self, A: List[int]) -> int:
    A.sort(reverse=True)
    n = len(A)
    for i in range(n - 2):
      if A[i] < A[i + 1] + A[i + 2]:
        return A[i] + A[i + 1] + A[i + 2]
    return 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.largestPerimeter(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
