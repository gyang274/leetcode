from typing import List

class Solution:
  def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
    # coordinate network quality
    def quality(x, y):
      q = 0
      for _x, _y, _q in towers:
        d = ((_x - x) ** 2 + (_y - y) ** 2) ** 0.5
        if d <= radius:
          q += int(_q / (1 + d))
      return q
    # determine the outside square
    xs = list(map(lambda p: p[0], towers))
    ys = list(map(lambda p: p[1], towers))
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    # coordinate maximize network quality 
    pmax, qmax = [0, 0], 0
    for x in range(xmin, xmax + 1):
      for y in range(ymin, ymax + 1):        
        q = quality(x, y)
        if q > qmax:
          pmax, qmax = [x, y], q
    return pmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[42,0,0]], 7),
    ([[23,11,21]], 9),
    ([[2,1,9],[0,1,9]], 2),
    ([[1,2,5],[2,1,7],[3,1,9]], 2),
    ([[1,2,13],[2,1,7],[0,1,9]], 2),
    ([[0,1,2],[2,1,2],[1,0,2],[1,2,2]], 1),
  ]
  rslts = [solver.bestCoordinate(towers, radius) for towers, radius in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
