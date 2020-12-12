from typing import List

class Solution:
  def solveSudoku(self, board: List[List[str]]) -> None:        
    """
    Key:
      A(i, j) is a member of R(i), C(j) and B(i // 3 * 3 + j // 3)
    """
    row = [set(("1", "2", "3", "4", "5", "6", "7", "8", "9")) for i in range(9)]
    col = [set(("1", "2", "3", "4", "5", "6", "7", "8", "9")) for j in range(9)]
    blk = [set(("1", "2", "3", "4", "5", "6", "7", "8", "9")) for k in range(9)]
    dot = []
    k = lambda i, j: i // 3 * 3 + j // 3
    for i in range(9):
      for j in range(9):
        z = board[i][j]
        if z == ".":
          dot.append([i, j])
        else:
          row[i].remove(z)
          col[j].remove(z)
          blk[k(i, j)].remove(z)
    
    aux = [[set() for j in range(9)] for i in range(9)]
    auz = [[set() for j in range(9)] for i in range(9)]
    for i in range(9):
      for j in range(9):
        aux[i][j] = set.intersection(row[i], col[j], blk[k(i, j)])
        auz[i][j] = set.intersection(row[i], col[j], blk[k(i, j)])
    
    n = len(dot)
    d = 0
    while d >= 0 and d < n:
      i = dot[d][0]
      j = dot[d][1]
      z = board[i][j]
      if not z == ".":
        board[i][j] = "."
        row[i].add(z)
        col[j].add(z)
        blk[k(i, j)].add(z)
      s = set.intersection(row[i], col[j], blk[k(i, j)], aux[i][j])
      if s:
        z = s.pop()
        board[i][j] = z
        aux[i][j].remove(z)
        row[i].remove(z)
        col[j].remove(z)
        blk[k(i, j)].remove(z)
        d += 1
      else:
        if not z == ".":
          aux[i][j] = auz[i][j].copy()
        d -= 1
    return None

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ],
  ]
  rslts = [solver.solveSudoku(board) for board in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")