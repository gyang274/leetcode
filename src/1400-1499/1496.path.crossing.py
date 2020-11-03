class Solution:
  def isPathCrossing(self, path: str) -> bool:
    # s: set of points visited
    x, y, s, d = 0, 0, {(0, 0)}, {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
    for p in path:
      dx, dy = d[p]
      x, y = x + dx, y + dy
      if (x, y) in s:
        return True
      s.add((x, y))
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "NES", "NESWW",
  ]
  rslts = [solver.isPathCrossing(path) for path in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
