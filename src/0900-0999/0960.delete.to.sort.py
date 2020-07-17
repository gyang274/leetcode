from typing import List

class Solution:
  def minDeletionSize(self, A: List[str]) -> int:
    # dynamic programming, O(MN^2)
    m, n = len(A), len(A[0])
    z = [1] * n
    for j in range(n):
      for i in range(j):
        if all(A[k][i] <= A[k][j] for k in range(m)):
          z[j] = max(z[j], z[i] + 1)
    return n - max(z)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["a"],
    ["ab"],
    ["a","b"],
    ["fedcba"],
    ["ghi","def","abc"],
    ["babca","bcazb","abcde"],
  ]
  rslts = [solver.minDeletionSize(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
