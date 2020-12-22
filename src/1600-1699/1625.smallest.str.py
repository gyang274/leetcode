class Solution:
  def findLexSmallestString(self, s: str, a: int, b: int) -> str:
    n = len(s)
    # bfs/dfs, brute-force..
    queue, seen = set([s]), set()
    while queue:
      x = queue.pop()
      # seen
      seen.add(x)
      # rotations by b..
      y = x[b:] + x[:b]
      if y not in seen:
        queue.add(y)
      # add a to odd index
      y = ''
      for i, m in enumerate(x):
        if i & 1:
          y += str((int(m) + a) % 10)
        else:
          y += m
      if y not in seen:
        queue.add(y)
    return min(seen)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    # "2050"
    ("5525", 9, 2),
    # "00553311"
    ("43987654", 7, 3),
    # "0014305132"
    ("5562438547", 1, 3),
  ]
  rslts = [solver.findLexSmallestString(s, a, b) for s, a, b in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
