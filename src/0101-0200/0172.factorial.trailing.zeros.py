class Solution:
  def trailingZeroes(self, n: int) -> int:
    """count num of factor 5 from 1 to n.
    """
    x = 0
    while n > 0:
      x += n // 5
      n //= 5
    return x