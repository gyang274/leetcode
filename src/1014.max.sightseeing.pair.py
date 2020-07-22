from typing import List

class Solution:
  def maxScoreSightseeingPair(self, A: List[int]) -> int:
    n = len(A)
    imax, smax = A[0] + 0, float("-inf")
    for j in range(1, n):
      smax = max(smax, imax + A[j] - j)
      imax = max(imax, A[j] + j)
    return smax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [8,5,2,7,1,4],
  ]
  rslts = [solver.maxScoreSightseeingPair(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
