class Solution:
  def hasAlternatingBits(self, n: int) -> bool:
    z = 1 ^ (n & 1)
    while n > 0:
      if not z ^ (n & 1):
        return False
      n >>= 1
      z = 1 ^ z
    return True

class Solution:
  def hasAlternatingBits(self, n: int) -> bool:
    return (n & (n >> 1)) == 0 and (n & (n >> 2)) == (n >> 2)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 10, 22, 42
  ]
  rslts = [solver.hasAlternatingBits(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
