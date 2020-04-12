from typing import List
from collections import defaultdict

class Solution:
  def leastBricks(self, wall: List[List[int]]) -> int:
    d = defaultdict(lambda: 0)
    # d: key by segment point where draw line won't across a brick on row r, max value -> min cross
    for w in wall:
      k = 0
      for i in range(len(w) - 1):
        k += w[i]
        d[k] += 1
    # minimal cross
    return len(wall) - max(d.values()) if d else len(wall)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1],[1],[1]],
    [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]],
  ]
  rslts = [solver.leastBricks(wall) for wall in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
