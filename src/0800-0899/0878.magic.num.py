class Solution:
  def _getGCD(self, x, y):
    while y:
      x, y = y, x % y
    return x
  def _getLCM(self, x, y):
    return x * y // self._getGCD(x, y)
  def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
    M = self._getLCM(A, B)
    K = M // A + M // B - 1
    L = sorted(set(range(0, M, A)) | set(range(0, M, B)))
    R, Q = N // K, N % K
    return (M * R + L[Q]) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 2, 3),
    (5, 2, 4),
    (3, 4, 6),
  ]
  rslts = [solver.nthMagicalNumber(N, A, B) for N, A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
