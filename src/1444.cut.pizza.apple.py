from typing import List
from functools import lru_cache

class Solution:
  @lru_cache(None)
  def recursive(self, i, j, k):
    if k == 1:
      return 1
    count = 0
    for u in range(i + 1, self.m):
      if self.x[i][j] - self.x[u][j] > 0 and self.x[u][j] >= k - 1:
        count += self.recursive(u, j, k - 1)
    for v in range(j + 1, self.n):
      if self.x[i][j] - self.x[i][v] > 0 and self.x[i][v] >= k - 1:
        count += self.recursive(i, v, k - 1)
    return count % (10 ** 9 + 7)
  def ways(self, pizza: List[str], k: int) -> int:
    m, n = len(pizza), len(pizza[0])
    # self.x[i][j]: num of apples on (i, j) and right and below
    self.x = list(map(lambda r: list(map(lambda a: 1 if a == 'A' else 0, r)), pizza))
    for i in range(m - 2, -1, -1):
      self.x[i][n - 1] += self.x[i + 1][n - 1]
    for j in range(n - 2, -1, -1):
      self.x[m - 1][j] += self.x[m - 1][j + 1]
    for i in range(m - 2, -1, -1):
      for j in range(n - 2, -1, -1):
        self.x[i][j] += self.x[i + 1][j] + self.x[i][j + 1] - self.x[i + 1][j + 1]
    self.m, self.n = m, n
    self.recursive.cache_clear()
    return self.recursive(0, 0, k)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["A..","AAA","..."], 3),
    (["A..","AA.","..."], 3),
    (["A..",".A.","..A"], 3),
    (["A..","AA.","..."], 1),
  ]
  rslts = [solver.ways(pizza, k) for pizza, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
