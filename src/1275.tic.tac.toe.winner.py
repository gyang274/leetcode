from typing import List
from collections import defaultdict

class Solution:
  def tictactoe(self, moves: List[List[int]]) -> str:
    # d: (player, dimenion<row/col/diag/hill>, row/col/diag/hill) -> num
    d = defaultdict(list)
    for i, (x, y) in enumerate(moves):
      p = 'B' if i & 1 else 'A'
      d[(p, 0, x)].append((x, y))
      if len(d[(p, 0, x)]) == 3:
        return p
      d[(p, 1, y)].append((x, y))
      if len(d[(p, 1, y)]) == 3:
        return p
      if x - y == 0:
        d[(p, 2)].append((x, y))
        if len(d[(p, 2)]) == 3:
          return p
      if x + y == 2:
        d[(p, 3)].append((x, y))
        if len(d[(p, 3)]) == 3:
          return p
    return 'Draw' if len(moves) == 9 else 'Pending'

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,0],[1,1]],
    [[0,0],[2,0],[1,1],[2,1],[2,2]],
    [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]],
    [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]],
  ]
  rslts = [solver.tictactoe(moves) for moves in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
