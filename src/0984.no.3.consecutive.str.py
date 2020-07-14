class Solution:
  def strWithout3a3b(self, A: int, B: int) -> str:
    n = A + B
    if A >= B:
      xs, xc, ys, yc = 'a', A, 'b', B
    else:
      xs, xc, ys, yc = 'b', B, 'a', A
    z, i = [''] * (xc + yc), 0
    while i < n:
      if xc > yc:
        z[i] = xs
        xc -= 1
        i += 1
        if xc > 0:
          z[i] = xs
          xc -= 1
          i += 1
        if yc > 0:
          z[i] = ys
          yc -= 1
          i += 1
      else:
        z[(i + 0)::2] = [xs] * xc
        z[(i + 1)::2] = [ys] * yc
        i = n
    return ''.join(z)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, 5),
    (3, 8),
    (5, 8),
  ]
  rslts = [solver.strWithout3a3b(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
