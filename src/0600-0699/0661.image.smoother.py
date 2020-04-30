class Solution:
  def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    n, m = len(M), len(M[0])
    S = [[0] * m for _ in range(n)]
    for i in range(n):
      for j in range(m):
        v, count = 0, 0
        for x in (i - 1, i, i + 1):
          if 0 <= x < n:
            for y in (j - 1, j, j + 1):
              if 0 <= y < m:
                v += M[x][y]
                count += 1
        S[i][j] = v // count
    return S