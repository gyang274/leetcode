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

class Solution:
  def _dist_to_next(self, x, y, n):
    """dist from x to y, x and y with same num of digits, given n.
    """
    count = 0
    while x <= n:
      count += min(n + 1, y) - x
      x *= 10
      y *= 10
    return count
  def findKthNumber(self, n: int, k: int) -> int:
    x = 1
    while k > 1:
      d = self._dist_to_next(x, x + 1, n)
      # print(f"{n=}, {k=}, {x=}, {d=}")
      if d > k - 1:
        x *= 10
        k -= 1
      else:
        k -= d
        x += 1
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (10, 3),
    (14, 2),
    (4089173, 3098723),
  ]
  rslts = [solver.findKthNumber(n, k) for n, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")