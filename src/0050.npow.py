class Solution:
  def myPow(self, x: float, n: int) -> float:
    if n < 0:
      return self.myPow(1 / x, -n)
    i = 0
    z = 1
    while n > 0:
      if n % 2:
        z *= x
      x *= x
      n //= 2
      i += 1
    return z


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    (2.0, 10),
    (2.0, -2),
    (2.0, 3),
    (0.00001, 2147483647)
  ]
  rslts = [solver.myPow(x, n) for x, n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")