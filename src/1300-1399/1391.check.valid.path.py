from typing import List

class DSU:
  def __init__(self):
    # representer
    self.reps = {}
  def add(self, x):
    self.reps[x] = x
  def find(self, x):
    if not x == self.reps[x]:
      self.reps[x] = self.find(self.reps[x])
    return self.reps[x]
  def union(self, x, y):
    self.reps[self.find(y)] = self.find(x)

class Solution:
  def hasValidPath(self, grid: List[List[int]]) -> bool:
    # dsu: disjoint set union
    # split each cell as - 9 sub-cells connected via grid value, refr Q0959
    # use (i, j) to represent grid, use <x, y> to represent split sub-cells
    # split (i, j) into <3 * i + 0/1/2, 3 * j + 0/1/2>, then
    # (0, 0) and (m - 1, n - 1) connected iff <1, 1> and <3 * (m - 1) + 1, 3 * (n - 1) + 1> connected
    m, n = len(grid), len(grid[0])
    dsu = DSU()
    # cnn: hash grid value -> left-upper, right-lower, (neighbor-grid-splitted-sub-cells-to-check..)
    cnn = {
      1: (( 0, -1), (0,  1), ((0, -2), )),
      2: ((-1,  0), (1,  0), ((-2, 0), )),
      3: (( 0, -1), (1,  0), ((0, -2), )),
      4: (( 0,  1), (1,  0), ()),
      5: ((-1,  0), (0, -1), ((0, -2), (-2, 0))),
      6: ((-1,  0), (0,  1), ((-2, 0), )),
    }
    for i in range(m):
      for j in range(n):
        # split
        x, y = 3 * i + 1, 3 * j + 1
        dsu.add((x, y))
        # union
        lu, rl, ncs = cnn[grid[i][j]]
        dsu.add((x + lu[0], y + lu[1]))
        dsu.add((x + rl[0], y + rl[1]))
        # connect sub-cells of this cell split
        dsu.union((x, y), (x + lu[0], y + lu[1]))
        dsu.union((x, y), (x + rl[0], y + rl[1]))
        # connect sub-cells with previous cells split
        for nc in ncs:
          if (x + nc[0], y + nc[1]) in dsu.reps:
            dsu.union((x, y), (x + nc[0], y + nc[1]))
    return dsu.find((1, 1)) == dsu.find((3 * (m - 1) + 1, 3 * (n - 1) + 1))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,1,2]],
    [[1,1,1,1,1,1,3]],
    [[1,2,1],[1,2,1]],
    [[2,4,3],[6,5,2]],
    [[2],[2],[2],[2],[2],[2],[6]],
  ]
  rslts = [solver.hasValidPath(grid) for grid in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")