class Solution:
  def angleClock(self, hour: int, minutes: int) -> float:
    h, m = hour % 12, minutes % 60
    hA, mA = h * 30 + m / 60 * 30, m * 6
    dA = abs(hA - mA)
    return min(dA, 360 - dA)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 58),
  ]
  rslts = [solver.angleClock(hour, minutes) for hour, minutes in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
