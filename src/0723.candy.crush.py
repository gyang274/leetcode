from typing import List

class Solution:
  def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
    m, n = len(board), len(board[0])    
    def find():
      found = False
      for i in range(m):
        for j in range(n - 2):
          if abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]) != 0:
            board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])
            found = True
      for i in range(m - 2):
        for j in range(n):
          if abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]) != 0:
            board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j])
            found = True
      return found
    def move():
      for j in range(n):
        k = m - 1
        for i in range(m - 1, -1, -1):
          if board[i][j] > 0:
            board[k][j] = board[i][j]
            k -= 1
        for k in range(k, -1, -1):
          board[k][j] = 0
      return None
    while find():
      move()
    return board

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      [110,5,112,113,114],
      [210,211,5,213,214],
      [310,311,3,313,314],
      [410,411,412,5,414],
      [5,1,512,3,3],
      [610,4,1,613,614],
      [710,1,2,713,714],
      [810,1,2,1,1],
      [1,1,2,2,2],
      [4,1,4,4,1014],
    ],
  ]
  rslts = [solver.candyCrush(board) for board in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
