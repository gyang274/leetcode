class Solution:
  def countNumbersWithUniqueDigits(self, n: int) -> int:
    """math
    """
    x, xn, n = 1, 1, min(n, 10)
    i = 1
    while i < n + 1:
      xn *= min(11 - i, 9)
      x += xn
      i += 1
    return x

class Solution:
  def countNumbersWithUniqueDigits(self, n: int) -> int:
    """dynamic programming
    """
    n = min(n, 10)
    x = [1] * (n + 1)
    for i in range(1, n + 1):
      x[i] = x[i - 1] * min(11 - i, 9)
    for i in range(1, n + 1):
      x[i] += x[i - 1]
    return x[n]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 2, 3, 5, 8, 13, 21, 34, 55,
  ]
  rslts = [solver.countNumbersWithUniqueDigits(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")