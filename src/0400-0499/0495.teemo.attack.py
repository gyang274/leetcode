from typing import List

class Solution:
  def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    x, e = 0, 0
    for t in timeSeries:
      x += max(0, min(t + duration - e, duration))
      e = max(e, t + duration)
    return x

class Solution:
  def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    n = len(timeSeries)
    if n == 0:
      return 0
    x = 0
    for i in range(n - 1):
      x += min(timeSeries[i + 1] - timeSeries[i], duration)
    return x + duration

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1, 2], 2),
    ([1, 4], 2),
  ]
  rslts = [solver.findPoisonedDuration(timeSeries, duration) for timeSeries, duration in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  
