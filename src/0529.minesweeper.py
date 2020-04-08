from typing import List

class Solution:
  def minesAround(self, i, j):
    dxdy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    mines, empty = 0, set([])
    for dx, dy in dxdy:
      x, y = i + dx, j + dy
      if 0 <= x < self.n and 0 <= y < self.m:
        if self.board[x][y] == "M":
          mines += 1
        elif self.board[x][y] == "E":
          empty.add((x, y))
    return mines, empty
  def click(self, i, j):
    mines, empty = self.minesAround(i, j)
    if mines == 0:
      self.board[i][j] = "B"
      for x, y in empty:
        self.click(x, y)
    else:
      self.board[i][j] = str(mines)
    return None
  def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
    i, j = click
    if board[i][j] == "M":
      board[i][j] = "X"
      return board
    else:
      # board[i][j] == "E"
      self.board, self.n, self.m = board, len(board), len(board[0])
      self.click(i, j)
      return self.board

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([
      ['E', 'E', 'E', 'E', 'E'],
      ['E', 'E', 'M', 'E', 'E'],
      ['E', 'E', 'E', 'E', 'E'],
      ['E', 'E', 'E', 'E', 'E']
    ], [3, 0]),
  ]
  rslts = [solver.updateBoard(board, click) for board, click in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
