from itertools import accumulate

class Solution:
  def __init__(self):
    self.md = list(accumulate([
      31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    ], initial = 0))
  def isLeapYear(self, y):
    return (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0)
  def daysFrom19710101(self, date):
    # Q1154 days of the year.
    y, m, d = map(int, date.split('-'))
    for i in range(1971, y):
      d += 365 + self.isLeapYear(i)
    return d + (m > 2 and self.isLeapYear(y)) + self.md[m - 1]
  def daysBetweenDates(self, date1: str, date2: str) -> int:
    return abs(self.daysFrom19710101(date1) - self.daysFrom19710101(date2))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("1985-03-03", "1990-09-26"),
  ]
  rslts = [solver.daysBetweenDates(date1, date2) for date1, date2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
