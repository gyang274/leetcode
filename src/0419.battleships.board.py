from typing import List

class Solution:
  def countBattleships(self, board: List[List[str]]) -> int:
    """one pass, TC: O(NM), SC: O(1).
    """
    n = 0
    for i in range(len(board)):
      for j in range(len(board[i])):
        if board[i][j] == "X" and (i == 0 or board[i - 1][j] == ".") and (j == 0 or board[i][j - 1] == "."):
          n += 1
    return n

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]],
  ]
  rslts = [solver.countBattleships(board) for board in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")