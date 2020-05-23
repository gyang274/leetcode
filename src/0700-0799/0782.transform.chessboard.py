from typing import List
from collections import Counter

class Solution:
  def movesToChessboard(self, board: List[List[int]]) -> int:
    """O(N^2), dimension reduction, check rows and cols separately.
    """
    n = len(board)
    ans = 0
    # count of rows/cols of different format
    for count in (Counter(map(tuple, board)), Counter(zip(*board))):
      # rows/cols can have and only have 2 format, 10101.. and 01010..
      if not (len(count) == 2 and all(x ^ y for x, y in zip(*count.keys())) and sorted(count.values()) == [n // 2, (n + 1) // 2]):
        return -1
      # x0: should 1st one be 10101.. (x0 = 1) or 01010.. (x0 = 0)
      # x0 must align with whichever has more counts when n is odd, otherwise doesn't matter when n is even
      line0, line1 = count
      x0s = [+(line0.count(1) * 2 > n)] if n % 2 else [0, 1]
      # nums of swaps to transform to ideal
      ans += min(sum((i - x) & 1 for i, x in enumerate(line0, x0)) for x0 in x0s) // 2
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]],
    [[0,1,0,1,0],[0,1,0,1,0],[1,0,1,0,1],[1,0,1,0,1],[1,0,1,0,1]],
  ]
  rslts = [solver.movesToChessboard(board) for board in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
