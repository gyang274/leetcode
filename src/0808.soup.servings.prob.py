class Solution:
  def recursive(self, i, j):
    if (i, j) not in self.memo:
      if i <= 0 and j <= 0:
        self.memo[(i, j)] = 0.5
      elif i <= 0 and j > 0:
        self.memo[(i, j)] = 1.0
      elif i > 0 and j <= 0:
        self.memo[(i, j)] = 0
      else:
        # i > 0 and j > 0
        self.memo[(i, j)] = 0.25 * (
          self.recursive(i - 100, j) + self.recursive(i - 75, j - 25) + self.recursive(i - 50, j - 50) + self.recursive(i - 25, j - 75)
        )
    return self.memo[(i, j)]
  def soupServings(self, N: int) -> float:
    if N > 5000:
      return 1.0
    self.memo = {}
    return self.recursive(N, N)