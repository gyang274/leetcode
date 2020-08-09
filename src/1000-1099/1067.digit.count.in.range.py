class Solution:
  def countDigitD(self, n: int, d: int) -> int:
    # Q0233, count num of digit d appearance on all positive integer x, 1 <= x <= n.
    count, m = 0, 1
    while n > m - 1:
      q, r = n // (10 * m), n % (10 * m)
      if d == 0:
        count += (q * m) if r >= m else ((q - 1) * m + r + 1)
      else:
        count += q * m + min(max(0, r - m * d + 1), m)
      m *= 10
    return count
  def digitsCount(self, d: int, low: int, high: int) -> int:
    return self.countDigitD(high, d) - self.countDigitD(low - 1, d)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (0, 23, 1080),
    (1, 42, 1080),
  ]
  rslts = [solver.digitsCount(d, low, high) for d, low, high in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")