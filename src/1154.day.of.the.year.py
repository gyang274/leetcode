from itertools import accumulate

class Solution:
  def __init__(self):
    self.md = list(accumulate([
      31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    ], initial = 0))
  def dayOfYear(self, date: str) -> int:
    y, m, d = list(map(int, date.split('-')))
    count = d + self.md[m - 1]
    if m > 2 and ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)):
      count += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.dayOfYear(date) for date in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
