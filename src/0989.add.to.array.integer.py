from typing import List

class Solution:
  def addToArrayForm(self, A: List[int], K: int) -> List[int]:
    i, k, n, A = 0, 0, len(A), A[::-1]
    while K or k:
      if i >= n:
        A.append(0)
      A[i] += K % 10 + k
      K //= 10
      k = A[i] // 10
      A[i] %= 10
      i += 1
    return A[::-1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,2,3], 7985),
  ]
  rslts = [solver.addToArrayForm(A, K) for A, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
