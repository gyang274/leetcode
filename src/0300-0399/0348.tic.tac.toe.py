from collections import Counter

class TicTacToe:
  
  def __init__(self, n: int):
    """Initialize your data structure here.
    """
    self.n = n
    # n rows, n cols, 1 main diagonal (dial), 1 anti diagonal (anti) to win the game
    # bitmask, use the nums 0..00 to represent player 1's or player 2's taken on the row, col and diag
    # win? if == 1..11, otherwise no win, each move up to 4 O(1) update and 4 O(1) comparisons
    # actually, no win at all can be checked and stop early, but no need here.
    self.count = collections.Counter()

  def move(self, row: int, col: int, player: int) -> int:
    """Player {player} makes a move at ({row}, {col}).
      @param row The row of the board.
      @param col The column of the board.
      @param player The player, can be either 1 or 2.
      @return The current winning condition, can be either:
              0: No one wins.
              1: Player 1 wins.
              2: Player 2 wins.
    """
    for rc, idx in enumerate((row, col, row+col, row-col)):
      self.count[rc, idx, player] += 1
      if self.count[rc, idx, player] == self.n:
        return player
    return 0

class TicTacToe:
  
  def __init__(self, n: int):
    """Initialize your data structure here.
    """
    self.n = n
    # n rows, n cols, 1 main diagonal (dial), 1 anti diagonal (anti) to win the game
    # bitmask, use the nums 0..00 to represent player 1's or player 2's taken on the row, col and diag
    # win? if == 1..11, otherwise no win, each move up to 4 O(1) update and 4 O(1) comparisons
    # actually, no win at all can be checked and stop early, but no need here.
    self.status = [
      # 2 players, each n rows, n cols, 1 dial, 1 anti.
      [[0] * n, [0] * n, 0, 0], [[0] * n, [0] * n, 0, 0],
    ]
    self.win = (1 << n) - 1

  def move(self, row: int, col: int, player: int) -> int:
    """Player {player} makes a move at ({row}, {col}).
      @param row The row of the board.
      @param col The column of the board.
      @param player The player, can be either 1 or 2.
      @return The current winning condition, can be either:
              0: No one wins.
              1: Player 1 wins.
              2: Player 2 wins.
    """
    # on r-th row, k-th col is taken by player
    self.status[player - 1][0][row] |= 1 << col
    if self.status[player - 1][0][row] == self.win:
      return player
    # on k-th col, r-th row is taken by player
    self.status[player - 1][1][col] |= 1 << row
    if self.status[player - 1][1][col] == self.win:
      return player
    # main diagonal
    if row == col:
      self.status[player - 1][2] |= 1 << col
      if self.status[player - 1][2] == self.win:
        return player
    # anti diagonal
    if row + col == self.n - 1:
      self.status[player - 1][3] |= 1 << row
      if self.status[player - 1][3] == self.win:
        return player
    # note: rows, cols, dial and anti, if already been taken by both, can be skipped for winning possible
    # this can be achieved/implemented by holding an additional bothTaken data.
    return 0