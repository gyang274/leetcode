class Solution:
  def numberOfDays(self, Y: int, M: int) -> int:
    # days in month
    ds = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # days in month
    d = ds[M - 1]
    # february
    if M == 2:
      if Y % 4 == 0:
        d += 1
      if Y % 100 == 0:
        d -= 1
      if Y % 400 == 0:
        d += 1
    return d

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1985, 3),
    (1988, 2),
    (1900, 2),
    (2000, 2),
  ]
  rslts = [solver.numberOfDays(Y, M) for Y, M in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")