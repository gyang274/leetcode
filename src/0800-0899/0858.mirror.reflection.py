class Solution:
  def _getGCD(self, x, y):
    while y:
      x, y = y, x % y
    return x
  # def _getLCM(self, x, y):
  #   return x * y // self._getGCD(x, y)
  def mirrorReflection(self, p: int, q: int) -> int:
    # imagine extend the line with square flipped horizontally and vertically until meet corner
    # (p, q) ->scale (1, q/p) ->extend (p/gcd(p,q), q/gcd(p,q))
    d = self._getGCD(p, q)
    p, q = p // d, q // d
    if q & 1:
      if p & 1:
        return 1
      else:
        return 2
    return 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 1),
    (3, 1),
    (3, 2),
    (4, 1),
    (4, 2),
    (4, 3),
  ]
  rslts = [solver.mirrorReflection(p, q) for p, q in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
