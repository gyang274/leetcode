from typing import List
from collections import defaultdict

class Solution:
  def countBitOne(self, x):
    count = 0
    while x:
      count += x & 1
      x >>= 1
    return count
  def maxStudents(self, seats: List[List[str]]) -> int:
    # bit mask of each row
    #  (x & (x >> 1)) == 0 to check if there are no adjancent valid states in x
    #  (x & (y >> 1)) == ((x >> 1) & y) == 0 to check no students in y at upper left/right position of x.
    m, n = len(seats), len(seats[0])
    # valid w.r.t to seats is ok to take
    vs = []
    for i in range(m):
      mask = 0
      for j in range(n):
        mask = (mask << 1) | (1 if seats[i][j] == '.' else 0)
      vs.append(mask)
    # valid w.r.t to no cheat on same row
    xs = {}
    for x in range(1 << n):
      if x & (x >> 1) == 0:
        xs[x] = self.countBitOne(x)
    # dp
    # dp[i][mask]: max num of students with 1st i-1 rows, with the (i-1)th row taken by mask.
    dp = defaultdict(lambda: defaultdict(lambda: 0))
    dp[0][0] = 0
    for i in range(m):
      v = vs[i]
      for x in xs:
        # x & v == x: means the 1s in bit representation of x is a subset of the 1s in bit representation of v
        if x & v == x:
          for y in xs:
            if (x & (y >> 1)) == ((x >> 1) & y) == 0:
              dp[i + 1][x] = max(dp[i + 1][x], dp[i][y] + xs[x])
    return max(dp[m].values())

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      [".","#"],
      ["#","#"],
      ["#","."],
      ["#","#"],
      [".","#"],
    ],
    [
      ["#",".",".",".","#"],
      [".","#",".","#","."],
      [".",".","#",".","."],
      [".","#",".","#","."],
      ["#",".",".",".","#"],
    ],
    [
      ["#",".","#","#",".","#"],
      [".","#","#","#","#","."],
      ["#",".","#","#",".","#"],
    ],
  ]
  rslts = [solver.maxStudents(seats) for seats in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
