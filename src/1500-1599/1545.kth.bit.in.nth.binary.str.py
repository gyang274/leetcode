class Solution:
  def findKthBit(self, n: int, k: int) -> str:
    f, k = 0, k
    while n > 1:
      m = 1 << (n - 1)
      if k == m:
        return str(1 ^ f)
      elif k > m:
        k = (1 << n) - k
        f = f ^ 1
      n -= 1
    return str(0 ^ f)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 0),
    (2, 0),
    (2, 3),
  ]
  rslts = [solver.findKthBit(n, k) for n, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
