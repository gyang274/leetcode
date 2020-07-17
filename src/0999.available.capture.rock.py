from typing import List

class Solution:
  def numRookCaptures(self, board: List[List[str]]) -> int:
    # rock
    for i in range(8):
      for j in range(8):
        if board[i][j] == 'R':
          u, v = i, j
          break
    # capture
    count = 0
    for i in range(u - 1, -1, -1):
      if board[i][v] == 'B':
        break
      if board[i][v] == 'p':
        count += 1
        break
    for i in range(u + 1, 8):
      if board[i][v] == 'B':
        break
      if board[i][v] == 'p':
        count += 1
        break
    for j in range(v - 1, -1, -1):
      if board[u][j] == 'B':
        break
      if board[u][j] == 'p':
        count += 1
        break
    for j in range(v + 1, 8):
      if board[u][j] == 'B':
        break
      if board[u][j] == 'p':
        count += 1
        break
    return count

class Solution:
  def numRookCaptures(self, board: List[List[str]]) -> int:
    return sum(''.join(r).replace('.', '').count('Rp') for r in board + list(zip(*board)) for r in [r, r[::-1]])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      [".",".",".",".",".",".",".","."],
      [".",".",".","p",".",".",".","."],
      [".",".",".","p",".",".",".","."],
      ["p","p",".","R",".","p","B","."],
      [".",".",".",".",".",".",".","."],
      [".",".",".","B",".",".",".","."],
      [".",".",".","p",".",".",".","."],
      [".",".",".",".",".",".",".","."]
    ],
  ]
  rslts = [solver.numRookCaptures(board) for board in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
