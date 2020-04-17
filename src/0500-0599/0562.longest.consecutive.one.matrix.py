from typing import List

class Solution:
  def longestLine(self, M: List[List[int]]) -> int:
    n = len(M)
    if n == 0:
      return 0
    m = len(M[0])
    if m == 0:
      return 0
    xmax = 0
    for i in range(n):
      for j in range(m):
        if M[i][j] == 1:
          # horizontal ones
          if j == 0 or M[i][j - 1] == 0:
            k = 1
            while j + k < m and M[i][j + k] == 1:
              k += 1
            xmax = max(xmax, k)
          # vertical ones
          if i == 0 or M[i - 1][j] == 0:
            k = 1
            while i + k < n and M[i + k][j] == 1:
              k += 1
            xmax = max(xmax, k)
          # diagonal ones
          if i == 0 or j == 0 or M[i - 1][j - 1] == 0:
            k = 1
            while i + k < n and j + k < m and M[i + k][j + k] == 1:
              k += 1
            xmax = max(xmax, k)
          # anti-digonal ones
          if i == 0 or j == m - 1 or M[i - 1][j + 1] == 0:
            k = 1
            while i + k < n and j - k >= 0 and M[i + k][j - k] == 1:
              k += 1
            xmax = max(xmax, k)
    return xmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      [0,1,1,0],
      [0,1,1,0],
      [0,0,0,1],
    ],
    [
      [1,1,1,1,1,1,0,1,1,1],
      [1,1,0,0,0,0,0,1,1,1],
      [0,1,0,1,1,1,1,0,0,0],
      [1,1,1,0,0,1,1,0,1,1],
      [1,0,1,1,1,0,1,1,1,1],
      [1,1,0,0,1,0,1,1,1,1],
      [1,0,1,0,0,0,1,1,0,1],
      [1,1,0,1,1,1,1,0,0,1],
      [1,1,1,1,0,0,0,1,1,0],
      [1,1,1,0,1,1,0,1,1,1],
    ]
  ]
  rslts = [solver.longestLine(M) for M in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
