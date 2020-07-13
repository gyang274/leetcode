from typing import List

class Solution:
  def maxTurbulenceSize(self, A: List[int]) -> int:
    # track count (I, D), I is turbulent with last one up, D is turbulent with last one down
    m, k, d, n = 1, 1, 1, len(A)
    for i in range(1, n):
      if A[i] == A[i - 1]:
        k = d = 1
      elif A[i] > A[i - 1]:
        k = d + 1
        d = 1
        m = max(k, m)
      else:
        d = k + 1
        k = 1
        m = max(d, m)
    return m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.maxTurbulenceSize(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
