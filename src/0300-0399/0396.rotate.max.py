from typing import List

class Solution:
  def maxRotateFunction(self, A: List[int]) -> int:
    """math: B_{k}[0] = A[-k]
      F(  k  ) - F(k - 1) = sum(A) - n * B_{ k }[0],
      F(k - 1) - F(k - 2) = sum(A) - n * B_{k-1}[0],
      ..
      F(k) - F(0) = k * sum(A) - n * sum(B_{k}[0], B_{k-1}[0], ... B_{1}[0])
      F(k) = F(0) + k * sum(A) - n * sum(A[-k], A[-(k-1)], .., A[-1])
    """
    n, sumA, fi = len(A), sum(A), sum([i * x for i, x in enumerate(A)])
    fmax = fi
    for i in range(1, n):
      fi = fi + sumA - n * A[-i]
      fmax = max(fmax, fi)
    return fmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [4, 3, 2, 6],
  ]
  rslts = [solver.maxRotateFunction(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
