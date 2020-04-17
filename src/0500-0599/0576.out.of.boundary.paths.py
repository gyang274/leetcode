class Solution:
  def recursive(self, i, j, N, m, n):
    if (i, j, N) not in self.memo:
      count = 0
      if N == 1:
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
          x, y = i + di, j + dj
          if x < 0 or x >= m or y < 0 or y >= n:
            count += 1
      else:
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
          x, y = i + di, j + dj
          if 0 <= x < m and 0 <= y < n:
            count += self.recursive(min(x, m - 1 - x), min(y, n - 1 - y), N - 1, m, n)
      self.memo[(i, j, N)] = count % (10 ** 9 + 7)
    return self.memo[(i, j, N)]
  def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
    i = min(i, m - 1 - i)
    j = min(j, n - 1 - j)
    self.memo = {}
    count = 0
    for Nk in range(1, N + 1):
      count += self.recursive(i, j, Nk, m, n)
    return count % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 2, 2, 0, 0),
    (42, 42, 47, 10, 10),
  ]
  rslts = [solver.findPaths(m, n, N, i, j) for m, n, N, i, j in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
