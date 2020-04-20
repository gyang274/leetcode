class Solution:
  def recursive(self, n, m, k):
    if not (n, m, k) in self.memo:
      if n < k or m < k:
        self.memo[(n, m, k)] = 0
      elif k == 1:
        self.memo[(n, m, k)] = 0
        for j in range(1, m + 1):
          self.memo[(n, m, k)] += j ** (n - 1)
      else:
        self.memo[(n, m, k)] = 0
        # recursive over last (k-th) update index and value.
        for i in range(k - 1, n):
          for j in range(k, m + 1):
            self.memo[(n, m, k)] += self.recursive(i, j - 1, k - 1) * (j ** (n - 1 - i))
      self.memo[(n, m, k)] %= (10 ** 9 + 7)
    return self.memo[(n, m, k)]
  def numOfArrays(self, n: int, m: int, k: int) -> int:
    self.memo = {}
    return self.recursive(n, m, k)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 3, 1),
    (5, 2, 3),
    (37, 17, 7),
    (50, 100, 25),
  ]
  rslts = [solver.numOfArrays(n, m, k) for n, m, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
