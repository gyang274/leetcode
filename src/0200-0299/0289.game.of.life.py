from typing import List

class Solution:
  def _score(self, i, j) -> int:
    dxdy = [
      ( 1,  0),
      ( 0,  1),
      (-1,  0),
      ( 0, -1),
      ( 1,  1),
      (-1,  1),
      (-1, -1),
      ( 1, -1),
    ]
    score = 0
    for dx, dy in dxdy:
      x = i + dx
      y = j + dy
      if 0 <= x < self.n and 0 <= y < self.m:
        score += self.board[x][y] % 2
    return score
  def gameOfLife(self, board: List[List[int]]) -> None:
    """Do not return anything, modify board in-place instead.
      This is like convolution with kernel 3x3 of all ones, then make decision w.r.t center is zero or one.
      Trick for in-place, use additional values to represent status change, say -1 as 1 -> 0 and 2 as 0 -> 1.
    """
    self.board = board
    self.n = len(self.board)
    if self.n == 0:
      return None
    self.m = len(self.board[0])
    if self.m == 0:
      return None
    # label
    for i in range(self.n):
      for j in range(self.m):
        s = self._score(i, j)
        if self.board[i][j] == 1:
          if s < 2 or s > 3:
            self.board[i][j] = -1
        else:
          # self.board[i][j] == 0
          if s == 3:
            self.board[i][j] = 2
    # parse
    for i in range(self.n):
      for j in range(self.m):
        # so, -1 or 0 -> 0, 1 or 2 -> 1
        self.board[i][j] = 0 if self.board[i][j] < 1 else 1
    return None

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      [0,1,0],
      [0,0,1],
      [1,1,1],
      [0,0,0]
    ],
  ]
  rslts = [solver.gameOfLife(board) for board in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")     

    