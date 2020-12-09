class Solution:
  def concatenatedBinary(self, n: int) -> int:
    x, M = 0, 10 ** 9 + 7
    for i in range(1, n + 1):
      x = ((x << (len(bin(i)) - 2)) + i) % M
    return x