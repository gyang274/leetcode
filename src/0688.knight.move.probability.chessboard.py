class Solution:
  def __init__(self):
    self.moves = [
      ( 1,  2),
      ( 1, -2),
      (-1,  2),
      (-1, -2),
      ( 2,  1),
      ( 2, -1),
      (-2,  1),
      (-2, -1),
    ]
  def recursive(self, N, K, r, c):
    # K >= 1
    if (N, K, r, c) not in self.memo:
      self.memo[(N, K, r, c)] = 0
      for dr, dc in self.moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
          self.memo[(N, K, r, c)] += 1 if K == 1 else self.recursive(N, K - 1, nr, nc)
        else:
          self.memo[(N, K, r, c)] += 0
      self.memo[(N, K, r, c)] /= 8
    return self.memo[(N, K, r, c)]
  def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
    if K == 0:
      return 1 if 0 <= r < N and 0 <= c < N else 0
    self.memo = {}
    return self.recursive(N, K, r, c)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, 2, 0, 0),
    (22, 42, 5, 8),
  ]
  rslts = [solver.knightProbability(N, K, r, c) for N, K, r, c in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
