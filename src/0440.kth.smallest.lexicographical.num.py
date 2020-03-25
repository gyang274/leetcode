class Solution:
  def recursive(self, z, i):
    for _ in range(10):
      x = next(z[i], None)
      if x:
        if len(self.ans) >= self.k:
          return None
        self.ans.append(x)
        if i + 1 < len(z):
          self.recursive(z, i + 1)
      else:
        z.pop()
        break
    return None
  def findKthNumber(self, n: int, k: int) -> int:
    """Q0386.
    """
    self.k = k
    # generators
    z, i = [], 1
    while i < n + 1:
      z.append(iter(range(i, min(n + 1, i * 10))))
      i *= 10
    # generators: call next recursively
    self.ans = []
    if z:
      self.recursive(z, 0)
    return self.ans[k - 1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (13, 2),
  ]
  rslts = [solver.findKthNumber(n, k) for n, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")