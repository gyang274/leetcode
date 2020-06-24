from typing import List

class Solution:
  def snakesAndLadders(self, board: List[List[int]]) -> int:
    n = len(board)
    # index to row and col
    i2rc = lambda i: ((n - 1) - (i - 1) // n, n - 1 - (i - 1) % n if ((i - 1) // n) & 1 else (i - 1) % n)
    queue, seen = [(0, 1)], {1}
    for d, i in queue:
      for j in range(1, 7):
        inext = i + j
        r, c = i2rc(i + j)
        if board[r][c] > -1:
          inext = board[r][c]
        if inext == n * n:
          return d + 1
        if inext not in seen:
          seen.add(inext)
          queue.append((d + 1, inext))
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,1,-1],[1,1,1],[-1,1,1]],
    [[-1,-1,-1],[-1,9,8],[-1,8,9]],
    [[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]],
    [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]],
    [[-1,-1,-1,-1,48,5,-1],[12,29,13,9,-1,2,32],[-1,-1,21,7,-1,12,49],[42,37,21,40,-1,22,12],[42,-1,2,-1,-1,-1,6],[39,-1,35,-1,-1,39,-1],[-1,36,-1,-1,-1,-1,5]],
    [[-1,60,32,-1,-1,-1,59,-1],[34,1,15,9,13,25,63,26],[-1,-1,-1,-1,29,-1,-1,-1],[-1,-1,-1,27,-1,-1,-1,5],[6,59,-1,2,40,13,-1,-1],[-1,44,20,-1,-1,-1,58,-1],[-1,-1,9,-1,-1,23,-1,-1],[-1,-1,-1,46,27,6,-1,-1]],
  ]
  rslts = [solver.snakesAndLadders(board) for board in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
