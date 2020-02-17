class Solution:
  def rangeBitwiseAnd(self, m: int, n: int) -> int:
    """common prefix of bin(m) and bin(n).
    """
    m2, n2 = bin(m)[2:], bin(n)[2:]
    if len(m2) < len(n2):
      return 0
    l2 = len(m2)
    i, x = 0, ""
    while i < l2 and m2[i] == n2[i]:
      x += m2[i]
      i += 1
    x += "0" * (l2 - i)
    return int(x, 2)

class Solution:
  def rangeBitwiseAnd(self, m: int, n: int) -> int:
    """common prefix of bin(m) and bin(n), so bit shift k until argmin_k(m >> k == n >> k), then shift back k.
    """
    k = 0
    while m < n:
      m >>= 1
      n >>= 1
      k += 1
    return m << k

class Solution:
  def rangeBitwiseAnd(self, m: int, n: int) -> int:
    """common prefix of bin(m) and bin(n), Brian Kernighan's algorithm, n & (n - 1) unset the rightmost 1 of bin(n).
      so repeat Brian Kernighan unitl n <= m, and in this way unset all trailing 1's of n not with m common prefix.
    """
    while m < n:
      n = n & (n - 1)
    return n

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (0, 0),
    (0, 1),
    (1, 3),
    (4, 7),
    (5, 7),
    (5, 11),
  ]
  rslts = [solver.rangeBitwiseAnd(m, n) for m, n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")