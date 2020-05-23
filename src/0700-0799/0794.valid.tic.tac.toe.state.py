from typing import List

class Solution:
  def validTicTacToe(self, board: List[str]) -> bool:
    z = ''.join(board)
    nX, nO = z.count('X'), z.count('O')
    if not (0 <= nX - nO <= 1):
      return False
    mX, mO = 0, 0
    for r in board:
      if r == 'XXX':
        mX += 1
      if r == 'OOO':
        mO += 1
    for c in zip(*board):
      c = ''.join(c)
      if c == 'XXX':
        mX += 1
      if c == 'OOO':
        mO += 1
    for d in (z[::4], z[2:7:2]):
      if d == 'XXX':
        mX += 1
      if d == 'OOO':
        mO += 1
    if mX * mO > 0:
      return False
    if mX > 0 and nX == nO:
      return False
    if mO > 0 and nX > nO:
      return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["   ", "   ", "   "],
    ["X  ", "   ", "   "],
    ["O  ", "   ", "   "],
    ["XOX", " X ", "   "],
    ["XXX", "   ", "OOO"],
    ["X O", "X O", "X O"],
    ["XXX", "XOO", "OO "],
    ["XXX", "OOX", "OOX"],
    ["XOO", "XXO", "XOX"],
    ["XOX", "O O", "XOX"],
  ]
  rslts = [solver.validTicTacToe(board) for board in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
