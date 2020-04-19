class Solution:
  def smallestFactorization(self, a: int) -> int:
    if a == 1:
      return 1
    b = ""
    for i in range(9, 1, -1):
      while (a % i == 0):
        b = str(i) + b
        a //= i
    if a > 1:
      return 0
    b = int(b)
    return b if b < (1 << 31) else 0
        