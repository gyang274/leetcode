from typing import List

class Solution:
  def numberOfArithmeticSlices(self, A: List[int]) -> int:
    """f(n) = 1 + 2 + .. + (n - 2), n >= 3, num of arithmetic slice for an arithmetic sequence of length n.
    """
    a, i, n = 0, 2, len(A)
    while i < n:
      if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
        j = 0
        while i + j < n and A[i + j] - A[i + j - 1] == A[i + j - 1] - A[i + j - 2]:
          j += 1
        a += j * (j + 1) // 2
        i += j
      else:
        i += 1
    return a

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1, 2, 3, 5, 8, 11, 14, 17, 22, 42, 43, 46, 49, 52, 55, 58, ],
  ]
  rslts = [solver.numberOfArithmeticSlices(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")