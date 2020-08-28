from datetime import datetime

class Solution:
  def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]    
    return days[datetime(y, m, d).weekday()]

class Solution:
  def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
    # O(1), Zeller's congruence or Kim Larsen calculation formula.
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", ]
    d, m, y = day, month, year
    if m < 3:
      m += 12
      y -= 1
    c, y = y // 100, y % 100
    w = (c // 4 - 2 * c + y + y // 4 + 13 * (m + 1) // 5 + d - 1) % 7
    return days[w]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, 3, 1985),
    (9, 26, 1990),
  ]
  rslts = [solver.dayOfTheWeek(day, month, year) for day, month, year in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
