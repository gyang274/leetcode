from typing import List

class Solution:
  def generateMatrix(self, n: int) -> List[List[int]]:
    x = [[0] * n for _ in range(n)]
    i, j, di, dj, k = 0, 0, 0, 1, 1
    while k <= n * n:
      x[i][j] = k
      if x[(i + di) % n][(j + dj) % n]:
        di, dj = dj, -di
      i += di
      j += dj
      k += 1
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 2, 3, 4, 5,
  ]
  rslts = [solver.generateMatrix(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")