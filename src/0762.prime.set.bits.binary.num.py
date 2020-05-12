class Solution:
  def countPrimeSetBits(self, L: int, R: int) -> int:
    p = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
    return sum(bin(x).count('1') in p for x in range(L, R + 1))