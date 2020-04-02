from collections import defaultdict

class Solution:
  def _cancellation(self, board):
    """remove all 3 consecutive same color, recursively.
    """
    if board not in self.memoBoard:
      i = 0
      while i < len(board):
        j = 0
        while i + j < len(board) and board[i] == board[i + j]:
          j += 1
        if j > 2:
          board = board[:i] + board[(i + j):]
          i = max(0, i - 2)
        else:
          i += 1
    return board
  def _handstr(self):
    s = ""
    for c in self.color:
      s += c + str(self.handc[c])
    return s
  def backtrack(self, board, ns):
    if board == "":
      self.ns = min(ns, self.ns)
    else:
      hs = self._handstr()
      if (board, hs) not in self.memoBoardHand:
        for c in self.color:
          if self.handc[c] > 0:
            for j in range(len(board) + 1):
              # should only insert same color adjacent to each color on board
              boardnext = self._cancellation(board[:j] + c + board[j:])
              self.handc[c] -= 1
              self.backtrack(boardnext, ns + 1)
              self.handc[c] += 1
        self.memoBoardHand.add((board, hs))
  def findMinStep(self, board: str, hand: str) -> int:
    """backtrack, brute force.
    """
    # color
    self.color = ["R", "Y", "B", "G", "W"]
    # hand as dict
    self.handc = defaultdict(lambda: 0)
    for c in hand:
      self.handc[c] += 1
    # preprocess:
    # 1. abandoned letters in hand but not in board
    for c in self.handc:
      if c not in board:
        self.handc[c] = 0
    # 2. -1 if count of a color less than 3 in board and hand
    for c in self.color:
      cc = board.count(c)
      if cc > 0 and self.handc[c] + cc < 3:
        return -1
    # memorization on board: board cancellation
    # memorization on (board, hands): hands as str: R_Y_B_G_W_
    self.memoBoard, self.memoBoardHand = {}, set([])
    # ns: num steps
    self.ns = len(hand) + 1
    # backtrack
    self.backtrack(board, 0)
    return -1 if self.ns == len(hand) + 1 else self.ns

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("G", "GGGGG"),
    ("WRRBBW", "RB"),
    ("RRWWRRBBRR", "WB"),
    ("WWRRBBWW", "WRBRW"),
    ("RBYYBBRRB", "YRBGB"),
  ]
  rslts = [solver.findMinStep(board, hand) for board, hand in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  
