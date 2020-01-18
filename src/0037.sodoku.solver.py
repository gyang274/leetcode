from typing import List


# class Solution:
#   def isValidSudoku(self, board: List[List[str]]) -> bool:
#     """
#     Key:
#       A(i, j) is a member of R(i), C(j) and B(i // 3 * 3 + j // 3)
#     """
#     row = [set(("1", "2", "3", "4", "5", "6", "7", "8", "9")) for x in range(9)]
#     col = [set(("1", "2", "3", "4", "5", "6", "7", "8", "9")) for x in range(9)]
#     blk = [set(("1", "2", "3", "4", "5", "6", "7", "8", "9")) for x in range(9)]
#     for i in range(9):
#       for j in range(9):
#         if board[i][j] == ".":
#           continue
#         elif board[i][j] in row[i] and board[i][j] in col[j] and board[i][j] in blk[i // 3 * 3 + j // 3]:
#           row[i].remove(board[i][j])
#           col[j].remove(board[i][j])
#           blk[i // 3 * 3 + j // 3].remove(board[i][j])
#         else:
#           return False
#     return True


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    # true
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
    # false
    [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
  ]
  rslts = [solver.isValidSudoku(board) for board in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")