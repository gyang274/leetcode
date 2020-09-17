from typing import List
from collections import deque

class Solution:
  def minFlips(self, mat: List[List[int]]) -> int:
    # use integer to represent the state
    m, n = len(mat), len(mat[0])
    x = 0
    for i in range(m):
      for j in range(n):
        if mat[i][j] == 1:
          x |= 1 << (i * n + j)
    mn = m * n
    # bfs, dfs, a-star search
    # bfs..
    q, seen = deque([(0, x)]), set()
    while q:
      s, x = q.popleft()
      if x == 0:
        return s
      if x not in seen:
        seen.add(x)
        # flip each one
        for k in range(mn):
          i, j, dks = k // n, k % n, [0]
          if i > 0:
            dks.append(-n)
          if i < m - 1:
            dks.append(+n)
          if j > 0:
            dks.append(-1)
          if j < n - 1:
            dks.append(+1)
          y = x
          for dk in dks:
            mask = 1 << (k + dk)
            if y & mask:
              # x at k-th is 1, set it to 0
              y &= ~mask
            else:
              # x at k-th is 0, set it to 1
              y |= mask
          q.append((s + 1, y))
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0]],
    [[0],[1],[1]],
    [[0,0],[0,1]],
    [[1,0,0],[1,0,0]],
    [[1,1,1],[1,0,1],[0,0,0]],
  ]
  rslts = [solver.minFlips(mat) for mat in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
