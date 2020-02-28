from typing import List

class Solution:
  def maximalRectangle(self, matrix: List[List[str]]) -> int:
    """Key:
      1. naive brute force O(N^3 M^3)
      2. modified Q0084 over each row O(N^2M)
      3. dynamic programming + Q0084 O(NM)
      4. dynamic programming on 3 directions O(NM)
    """
    # Key: suppose max rectangle is w * h, then must at some index, such that height i - u + 1 is exactly h, 
    #   and when extend from i to left and right is w = (r - l + 1), all 1 and each l <= j <= r has height >= h.
    n = len(matrix)
    if n == 0:
      return 0
    m = len(matrix[0])
    if m == 0:
      return 0
    # dp of (u, l, r):
    #  u: upper index such that u \\ i all 1
    #  l: left index such that l -- i all 1, and all j such that l <= j <= i have u \\ j all 1
    #  r: right index such that i -- r all 1, and all j such that i <= j <= r have u \\ j all 1
    dp = [[[None, None, None] for _ in range(m)] for _ in range(n)]
    # |v u
    for j in range(m):
      u = 0
      for i in range(n):
        if matrix[i][j] == '1':
          dp[i][j][0] = u
        else:
          u = i + 1
    # print('u matrix')
    # for i in range(n):
    #   print([dp[i][j][0] for j in range(m)])
    # -> l, w.r.t u, stack of left up trending wall like in Q0084
    for i in range(n):
      # l stack store left trending wall index and upper index
      l = [(-1, n)]
      for j in range(m):
        if matrix[i][j] == '1':
          if dp[i][j][0] < l[-1][1]:
            l.append((j, dp[i][j][0]))
            dp[i][j][1] = j
          else:
            k, u = l[-1][0], l[-1][1]
            while dp[i][j][0] > l[-1][1]:
              k, u = l.pop()
            if dp[i][j][0] == l[-1][1]:
              dp[i][j][1] = l[-1][0]
            else:
              dp[i][j][1] = k
              if u == n:
                l.append((j, dp[i][j][0]))
              else:
                l.append((k, dp[i][j][0]))
        else:
          l = [(j, n)]
    # print('l matrix')
    # for i in range(n):
    #   print([dp[i][j][1] for j in range(m)])
    # r <-, w.r.t u, stack of right up trending wall like in Q0084
    for i in range(n):
      # r stack store right trending wall index and upper index
      r = [(m, n)]
      for j in range(m - 1, -1, -1):
        if matrix[i][j] == '1':
          if dp[i][j][0] < r[-1][1]:
            r.append((j, dp[i][j][0]))
            dp[i][j][2] = j
          else:
            k, u = r[-1][0], r[-1][1]
            while dp[i][j][0] > r[-1][1]:
              k, u = r.pop()
            if dp[i][j][0] == r[-1][1]:
              dp[i][j][2] = r[-1][0]
            else:
              dp[i][j][2] = k
              if u == n:
                r.append((j, dp[i][j][0]))
              else:
                r.append((k, dp[i][j][0]))
        else:
          r = [(j, n)]
    # print('r matrix')
    # for i in range(n):
    #   print([dp[i][j][2] for j in range(m)])
    # area
    smax = 0
    for i in range(n):
      for j in range(m):
        if matrix[i][j] == '1':
          smax = max(smax, (i - dp[i][j][0] + 1) * (dp[i][j][2] - dp[i][j][1] + 1))
    return smax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ],
    [
      ["0","0","0","1","0","1","1","1"],
      ["0","1","1","0","0","1","0","1"],
      ["1","0","1","1","1","1","0","1"],
      ["0","0","0","1","0","0","0","0"],
      ["0","0","1","0","0","0","1","0"],
      ["1","1","1","0","0","1","1","1"],
      ["1","0","0","1","1","0","0","1"],
      ["0","1","0","0","1","1","0","0"],
      ["1","0","0","1","0","0","0","0"]
    ],
    [
      ["0","1","1","0","0","1","0","1","0","1"],
      ["0","0","1","0","1","0","1","0","1","0"],
      ["1","0","0","0","0","1","0","1","1","0"],
      ["0","1","1","1","1","1","1","0","1","0"],
      ["0","0","1","1","1","1","1","1","1","0"],
      ["1","1","0","1","0","1","1","1","1","0"],
      ["0","0","0","1","1","0","0","0","1","0"],
      ["1","1","0","1","1","0","0","1","1","1"],
      ["0","1","0","1","1","0","1","0","1","1"]
    ],
  ]
  rslts = [solver.maximalRectangle(matrix) for matrix in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")