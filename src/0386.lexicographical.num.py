from typing import List

class Solution:
  def recursive(self, z, i):
    for _ in range(10):
      x = next(z[i], None)
      if x:
        self.ans.append(x)
        if i + 1 < len(z):
          self.recursive(z, i + 1)
      else:
        z.pop()
        break
    return None
  def lexicalOrder(self, n: int) -> List[int]:
    # generators
    z, i = [], 1
    while i < n + 1:
      z.append(iter(range(i, min(n + 1, i * 10))))
      i *= 10
    # generators: call next recursively
    self.ans = []
    if z:
      self.recursive(z, 0)
    return self.ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, 42, 128, 1024,
  ]
  rslts = [solver.lexicalOrder(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")