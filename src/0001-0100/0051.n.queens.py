from typing import List

import copy


class Solution:
  def backtrack(self, ans, queens, board, n):
    if len(queens) >= n:
      ans.append(queens)
    else:
      i = len(queens)
      for j in range(n):
        if board[i][j] == 0:
          boardCopy = copy.deepcopy(board)
          for k in range(n):
            boardCopy[i][k] = 1
            boardCopy[k][j] = 1
            if i + k < n and j + k < n:
              boardCopy[i + k][j + k] = 1
            if i - k >= 0 and j - k >= 0:
              boardCopy[i - k][j - k] = 1
            if i + k < n and j - k >= 0:
              boardCopy[i + k][j - k] = 1
            if i - k >= 0 and j + k < n:
              boardCopy[i - k][j - k] = 1
          self.backtrack(ans, queens + [j], boardCopy, n)
  def solveNQueens(self, n: int) -> List[List[str]]:
    """backtrack
    """
    ans, queens = [], []
    board = [[0] * n for _ in range(n)]
    self.backtrack(ans, queens, board, n)
    ans = [['.' * queen + 'Q' + '.' * (n - 1 - queen) for queen in queens] for queens in ans]
    return ans


class Solution:
  def backtrack(self, ans, row, col, hill, dale, n):
    i = len(row)
    for j in range(n):
      print(f"{n=}, {i=}, {j=}, ")
      if col[j] == 0 and hill[i + j] == 0 and dale[i - j] == 0:
        row.append(j)
        col[j] = 1
        hill[i + j] = 1
        dale[i - j] = 1
        if len(row) == n:
          ans.append(row.copy())
        else:
          self.backtrack(ans, row, col, hill, dale, n)
        row.remove(j)
        col[j] = 0
        hill[i + j] = 0
        dale[i - j] = 0
  def solveNQueens(self, n: int) -> List[List[str]]:
    """backtrack
      improvement 1: use row, col, hill and dale diagonals to replace board
        row: a list of n, at each index i, store the i-th row's queen position
        col: a list of n, at each index j, store whether or not j-th col has been taken.
        hill, dale: a list of (2n - 1), at each index k, store whether or not k-th diagonal has been taken.
    """
    ans, row, col, hill, dale = [], [], [0] * n, [0] * (2 * n  - 1), [0] * (2 * n - 1)
    self.backtrack(ans, row, col, hill, dale, n)
    ans = [['.' * k + 'Q' + '.' * (n - 1 - k) for k in row] for row in ans]
    return ans


class Solution:
  def backtrack(self, ans, rows, cols, hill, rowNext, dale, n):
    if len(rows) == n:
      ans.append(rows)
    else:
      colLeft = cols & ~(hill | rowNext | dale)
      while colLeft:
        colTook = -colLeft & colLeft
        colLeft ^= colTook
        self.backtrack(ans, rows + [len(bin(colTook)) - 3], cols, (hill | colTook) << 1, rowNext | colTook, (dale | colTook) >> 1, n)

  def solveNQueens(self, n: int) -> List[List[str]]:
    """backtrack
      improvement 1: use row, col, hill and dale diagonals to replace board
        row: a list of n, at each index i, store the i-th row's queen position
        col: a list of n, at each index j, store whether or not j-th col has been taken.
        hill, dale: a list of (2n - 1), at each index k, store whether or not k-th diagonal has been taken.
      improvement 2: use bitmap to represent row, col, hill and dale diagonals
    """
    ans, rows, cols, hill, rowNext, dale = [], [], (1 << n) - 1, 0, 0, 0
    self.backtrack(ans, rows, cols, hill,rowNext, dale, n)
    ans = [['.' * k + 'Q' + '.' * (n - 1 - k) for k in row] for row in ans]
    return ans


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    0,
    1,
    2,
    3,
    4,
    5,
  ]
  rslts = [solver.solveNQueens(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")