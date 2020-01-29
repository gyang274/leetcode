class Solution:
  def mySqrt(self, x: int) -> int:
    """Newton's Method.
      f(y) = y**2 - x = 0
      f(y1) = f(y0) + dy * f'(y0) = y0 * y0 - x + (y1 - y0) * 2 * y0 = 0
      y1 = (y0 + x / y0) / 2
    """
    if x == 0:
      return 0
    d = 0.1
    y = x / 2
    z = (y + x/y) / 2
    e = abs(z-y)
    while e > d:
      y = z
      z = (y + x/y) / 2
      e = abs(z - y)
    return int(z)


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    4,
    8,
    0,
    1,
  ]
  rslts = [solver.mySqrt(x) for x in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")