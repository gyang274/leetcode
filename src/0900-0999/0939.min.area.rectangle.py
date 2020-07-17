from typing import List
from collections import defaultdict

class Solution:
  def minAreaRect(self, points: List[List[int]]) -> int:
    d = defaultdict(set)
    for x, y in points:
      d[x].add(y)
    xs = sorted(d.keys())  
    m, n = float('inf'), len(xs)
    for i in range(n):
      for j in range(i):
        ys = sorted(d[xs[i]] & d[xs[j]])
        if len(ys) > 1:
          m = min(m, abs(xs[i] - xs[j]) * min(y1 - y2 for y1, y2 in zip(ys[1:], ys[:-1])))
    return 0 if m == float('inf') else m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,1],[1,3],[3,1],[3,3],[2,2]],
    [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]],
    [[3,2],[3,1],[4,4],[1,1],[4,3],[0,3],[0,2],[4,0]]
  ]
  rslts = [solver.minAreaRect(points) for points in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
