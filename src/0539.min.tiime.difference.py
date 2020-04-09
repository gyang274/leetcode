from typing import List

class Solution:
  def minuteOfDay(self, t):
    hh, mm = t.split(":")
    return int(hh) * 60 + int(mm)
  def findMinDifference(self, timePoints: List[str]) -> int:
    xmin, n = 1440, len(timePoints)
    minutes = sorted(map(self.minuteOfDay, timePoints))
    for i in range(n):
      xmin = min((minutes[(i + 1) % n] - minutes[i]) % 1440, xmin)
    return xmin

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["23:59","00:00"],
  ]
  rslts = [solver.findMinDifference(timePoints) for timePoints in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
