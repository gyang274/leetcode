from typing import List
from collections import defaultdict

class Solution:
  def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
    n = len(releaseTimes)
    for i in range(n - 1, 0, -1):
      releaseTimes[i] -= releaseTimes[i - 1]
    d = defaultdict(lambda: 0)
    for x, t in zip(keysPressed, releaseTimes):
      d[x] = max(d[x], t)
    m = max(d.values())
    return max(x for x in d if d[x] == m)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([9,29,49,50], 'cbcb'),
  ]
  rslts = [solver.slowestKey(releaseTimes, keysPressed) for releaseTimes, keysPressed in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
