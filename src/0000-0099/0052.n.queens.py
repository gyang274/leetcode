class Solution:
  def backtrack(self, rows, cols, hill, rowNext, dale, n):
    if rows == n:
      self.count += 1
    else:
      colLeft = cols & ~(hill | rowNext | dale)
      while colLeft:
        # right most 1 in binary format, e,g., 10100 -> 100, 
        # this is becuase bin(x) + bin(-x) => all 0 with overflow 1,
        # so bin(x) last 1 get bin(-x) last 1, and both 0 on right, and 0, 1 each on left
        colTook = -colLeft & colLeft
        colLeft ^= colTook
        self.backtrack(rows + 1, cols, (hill | colTook) << 1, rowNext | colTook, (dale | colTook) >> 1, n)
  def totalNQueens(self, n: int) -> int:
    """backtrack
      improvement 1: use row, col, hill and dale diagonals to replace board
        row: a list of n, at each index i, store the i-th row's queen position
        col: a list of n, at each index j, store whether or not j-th col has been taken.
        hill, dale: a list of (2n - 1), at each index k, store whether or not k-th diagonal has been taken.
      improvement 2: use bitmap to represent row, col, hill and dale diagonals
    """
    self.count, rows, cols, hill, rowNext, dale = 0, 0, (1 << n) - 1, 0, 0, 0
    self.backtrack(rows, cols, hill,rowNext, dale, n)
    return self.count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
  ]
  rslts = [solver.totalNQueens(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")