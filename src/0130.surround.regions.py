from typing import List

class Solution:
  def solve(self, board: List[List[str]]) -> None:
    """Do not return anything, modify board in-place instead.
    """
    m = len(board)
    if m == 0:
      return None
    n = len(board[0])
    # outer 'O'
    outer = set()
    for j in range(n):
      if board[0][j] == 'O':
        outer.add((0, j))
      if board[m - 1][j] == 'O':
        outer.add((m - 1, j))
    for i in range(1, m - 1):
      if board[i][0] == 'O':
        outer.add((i, 0))
      if board[i][n - 1] == 'O':
        outer.add((i, n - 1))
    # all 'O' connected to outer
    connected,  stack = outer.copy(), outer
    dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while stack:
      sx, sy = stack.pop()
      for dx, dy in dxdy:
        x, y = sx + dx, sy + dy
        if 0 <= x < m and 0 <= y < n and board[x][y] == 'O' and (x, y) not in connected:
          connected.add((x, y))
          stack.add((x, y))
    # flipped inner 'O' to 'X'
    for i in range(1, m - 1):
      for j in range(1, n  - 1):
        if board[i][j] == 'O' and (i, j) not in connected:
          board[i][j] = 'X'
    return None

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [
      ["X","X","X","X"],
      ["X","O","O","X"],
      ["X","X","O","X"],
      ["X","O","X","X"]
    ],
  ]
  rslts = [solver.solve(board) for board in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")