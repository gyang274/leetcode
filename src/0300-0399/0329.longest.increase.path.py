from typing import List
from functools import lru_cache

class Solution:
  def __init__(self):
    self.dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
  def isMinAround(self, i, j):
    """(i, j) is one of the min of neighbours or not.
    """
    for dx, dy in self.dxdy:
      x, y = i + dx, j + dy
      if 0 <= x < self.n and 0 <= y < self.m and self.matrix[x][y] < self.matrix[i][j]:
        return False
    return True
  def dfs(self, i, j):
    if (i, j) not in self.memo:
      self.memo[(i, j)] = 1
      for dx, dy in self.dxdy:
        x, y = i + dx, j + dy
        if 0 <= x < self.n and 0 <= y < self.m and self.matrix[x][y] > self.matrix[i][j]:
          self.memo[(i, j)] = max(self.memo[(i, j)], 1 + self.dfs(x, y))  
    return self.memo[(i, j)]
  def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    self.matrix = matrix
    # init
    self.n = len(self.matrix)
    if self.n == 0:
      return 0
    self.m = len(self.matrix[0])
    if self.m == 0:
      return 0
    # dfs with memo
    self.l, self.memo = 0, {}
    for i in range(self.n):
      for j in range(self.m):
        if self.isMinAround(i, j):
          self.l = max(self.l, self.dfs(i, j))
    return self.l

class Solution:
  def __init__(self):
    self.dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
  def dfs(self, i, j):
    if (i, j) not in self.memo:
      self.memo[(i, j)] = 1
      for dx, dy in self.dxdy:
        x, y = i + dx, j + dy
        if 0 <= x < self.n and 0 <= y < self.m and self.matrix[x][y] > self.matrix[i][j]:
          self.memo[(i, j)] = max(self.memo[(i, j)], 1 + self.dfs(x, y))  
    return self.memo[(i, j)]
  def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    self.matrix = matrix
    # init
    self.n = len(self.matrix)
    if self.n == 0:
      return 0
    self.m = len(self.matrix[0])
    if self.m == 0:
      return 0
    # dfs with memorization
    self.l, self.memo = 0, {}
    for i in range(self.n):
      for j in range(self.m):
        self.l = max(self.l, self.dfs(i, j))
    return self.l

class Solution:
  @lru_cache(None)
  def dfs(self, i, j):
    ans = 1
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
      x, y = i + dx, j + dy
      if 0 <= x < self.n and 0 <= y < self.m and self.matrix[x][y] > self.matrix[i][j]:
        ans = max(ans, 1 + self.dfs(x, y))  
    return ans
  def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    self.matrix = matrix
    # init
    self.n = len(self.matrix)
    if self.n == 0:
      return 0
    self.m = len(self.matrix[0])
    if self.m == 0:
      return 0
    # dfs with memorization
    ans = 0
    self.dfs.cache_clear()
    for i in range(self.n):
      for j in range(self.m):
        ans = max(ans, self.dfs(i, j))
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      [9,9,4],
      [6,6,8],
      [2,1,1],
    ],
    [
      [3,4,5],
      [3,2,6],
      [2,2,1],
    ],
    [
      [0,1,2,3,4,5,6,7,8,9],
      [19,18,17,16,15,14,13,12,11,10],
      [20,21,22,23,24,25,26,27,28,29],
      [39,38,37,36,35,34,33,32,31,30],
      [40,41,42,43,44,45,46,47,48,49],
      [59,58,57,56,55,54,53,52,51,50],
      [60,61,62,63,64,65,66,67,68,69],
      [79,78,77,76,75,74,73,72,71,70],
      [80,81,82,83,84,85,86,87,88,89],
      [99,98,97,96,95,94,93,92,91,90],
      [100,101,102,103,104,105,106,107,108,109],
      [119,118,117,116,115,114,113,112,111,110],
      [120,121,122,123,124,125,126,127,128,129],
      [139,138,137,136,135,134,133,132,131,130],
      [0,0,0,0,0,0,0,0,0,0]
    ],
  ]
  rslts = [solver.longestIncreasingPath(matrix) for matrix in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")