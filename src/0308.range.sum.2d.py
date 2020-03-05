from typing import List

class NumMatrix:
  """Sqrt Decomposition, TC: O(sqrt(rows x cols)).
  """
  def __init__(self, matrix: List[List[int]]):
    return None

  def update(self, row: int, col: int, val: int) -> None:
    return None

  def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    return None

class NumMatrix:
  """Row/Col Decomposition, TC: update O(cols), sum region O(rows).
    Keep cumulative sum over each row, update along the row so O(cols), sum over rows so O(rows).
  """
  def __init__(self, matrix: List[List[int]]):
    return None

  def update(self, row: int, col: int, val: int) -> None:
    return None

  def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    return None

class NumMatrix:
  """Segment Tree 2D: update (logN*logM), sum region (logN*logM), SC: O(4NM)
  """
  def __init__(self, matrix: List[List[int]]):
    if len(matrix) == 0:
      return None
    if len(matrix[0]) == 0:
      return None
    self.n, self.m = len(matrix), len(matrix[0])
    # segment tree 2d
    self.st = [[None] * self.m * 2 for i in range(self.n)] + [[None] * self.m + matrix[i] for i in range(self.n)]
    # segment tree 1d as componenet
    for i in range(self.n, self.n * 2):
      for j in range(self.m - 1, 0, -1):
        self.st[i][j] = self.st[i][2 * j] + self.st[i][2 * j + 1]
    # segment tree 2d use segment tree 1d as component
    for i in range(self.n - 1, 0, -1):
      for j in range(1, self.m * 2):
        self.st[i][j] = self.st[2 * i][j] + self.st[2 * i + 1][j]
    # segment tree 2d is O(2n * 2m)
    # for i in range(self.n * 2):
    #   print(self.st[i])

  def update(self, row: int, col: int, val: int) -> None:
    # locate the base cell (kr, kc), value and difference
    kr, kc, diff = self.n + row, self.m + col, val - self.st[self.n + row][self.m + col]
    # propagate the update along the rows, and along cols within each row kr
    while kr > 0:
      rc = kc
      while rc > 0:
        self.st[kr][rc] += diff
        rc //= 2
      kr //= 2
    # for i in range(self.n * 2):
    #   print(self.st[i])
    return None

  def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    rl, rr, cl, cr, xsum = self.n + row1, self.n + row2, self.m + col1, self.m + col2, 0
    while rl <= rr:
      # move rl along 2nd dimension
      if rl % 2 == 0:
        rl //= 2
      else:
        # collect over 1st dimension
        rcl, rcr = cl, cr
        while rcl <= rcr:
          if rcl % 2 == 0:
            rcl //= 2
          else:
            xsum += self.st[rl][rcl]
            # print(f"{rl=}, {rcl=}, {self.st[rl][rcl]=}, {xsum=}")
            rcl = (rcl + 1) // 2
          if rcr % 2 == 1:
            rcr //= 2
          else:
            xsum += self.st[rl][rcr]
            # print(f"{rl=}, {rcr=}, {self.st[rl][rcr]=}, {xsum=}")
            rcr = (rcr - 1) // 2
        # print(f"{rl=}, {xsum=}")
        rl = (rl + 1) // 2
      # move rr along 2nd dimension
      if rr % 2 == 1:
        rr //= 2
      else:
        # collect over 1st dimension
        rcl, rcr = cl, cr
        while rcl <= rcr:
          if rcl % 2 == 0:
            rcl //= 2
          else:
            xsum += self.st[rr][rcl]
            # print(f"{rr=}, {rcl=}, {self.st[rl][rcl]=}, {xsum=}")
            rcl = (rcl + 1) // 2
          if rcr % 2 == 1:
            rcr //= 2
          else:
            xsum += self.st[rr][rcr]
            # print(f"{rr=}, {rcr=}, {self.st[rr][rcr]=}, {xsum=}")
            rcr = (rcr - 1) // 2
        # print(f"{rr=}, {xsum=}")
        rr = (rr - 1) // 2
    return xsum

if __name__ == '__main__':
  # test1
  solver = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
  cases = [
    ("sumRegion", [2,1,4,3]),
    ("update", [3,2,2]),
    ("sumRegion", [2,1,4,3]),
  ]
  rslts = [eval(f"solver.{action}(*{param})") for action, param in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
  # test2
  solver = NumMatrix([[1,2]])
  cases = [
    ("sumRegion", [0,0,0,0]),
    ("sumRegion", [0,1,0,1]),
    ("sumRegion", [0,0,0,1]),
    ("update", [0,0,3]),
    ("sumRegion", [0,0,0,1]),
    ("update", [0,1,5]),
    ("sumRegion", [0,0,0,1]),
  ]
  rslts = [eval(f"solver.{action}(*{param})") for action, param in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
