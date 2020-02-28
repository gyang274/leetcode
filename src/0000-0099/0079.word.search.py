from typing import List


class Solution:
  def backtrack(self, i, j, word):
    if word == "":
      return True
    if 0 <= i < self.n and 0 <= j < self.m and self.board[i][j] == word[0]:
      # mark the match to prevent double match on the same position
      self.board[i][j] = '#'
      for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if self.backtrack(i + di, j + dj, word[1:]):
          return True
      self.board[i][j] = word[0]
    return False
  def exist(self, board: List[List[str]], word: str) -> bool:
    self.n, self.m, self.board = len(board), len(board[0]), board
    for i in range(self.n):
      for j in range(self.m):
        if self.backtrack(i, j, word):
          return True
    return False



if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ], 'ABCCED'),
    ([
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ], 'SEE'),
    ([
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ], 'ABCB'),
  ]
  rslts = [solver.exist(board, word) for board, word in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")