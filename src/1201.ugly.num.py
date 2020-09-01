class Solution:
  def _getGCD(self, x, y):
    while y:
      x, y = y, x % y
    return x
  def _getLCM(self, x, y):
    return x * y // self._getGCD(x, y)
  def _numDivisibleABC(self, n, a, b, c):
    """num of integers <= n that is divisible by a or b or c using inclusive-exclusive aka Venn Diagram.
    """
    ab = self._getLCM(a, b)
    bc = self._getLCM(b, c)
    ca = self._getLCM(c, a)
    abc = self._getLCM(ab, c)
    return n // a + n // b + n // c - n // ab - n // bc - n // ca + n // abc
  def _isUgly(self, n, a, b, c):
    return n % a == 0 or n % b == 0 or n % c == 0
  def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
    """modified binary search, not similar to Q0263, Q0264, Q0313.
    """
    l, m, r = n, n, n
    # binary search to identify r
    while self._numDivisibleABC(r, a, b, c) < n:
      r *= 2
    # binary search to identify m
    # m: some one such that number of integer <= m divisible by a, b, or c is n
    while l <= r:
      m = l + (r - l) // 2
      if self._numDivisibleABC(m, a, b, c) == n:
        break
      elif self._numDivisibleABC(m, a, b, c) < n:
        l = m + 1
      else:
        r = m - 1
    # binary search to identify x
    # x: make sure what is return is divisiable by a, b, or c
    if not self._isUgly(m, a, b, c):
      l, r = m - min(a, b, c), m
      while l <= r:
        m = l + (r - l) // 2
        if self._numDivisibleABC(m, a, b, c) == n:
          if self._isUgly(m, a, b, c):
            break
          else:
            r = m - 1
        else:
          l = m + 1
    return m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 2, 3, 5),
    (4, 2, 3, 4),
    (10, 2, 3, 5),
    (10, 2, 3, 6),
    (42, 2, 3, 14),
    (1000000000, 2, 217983653, 336916467),
  ]
  rslts = [solver.nthUglyNumber(n, a, b, c) for n, a, b, c in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
