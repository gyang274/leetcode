import math

class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    while n > 1:
      if n % 3 == 0:
        n //= 3
      else:
        return False
    return n == 1

class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    # pow(3, int(math.log(1 << 31) / math.log(3))) = 1162261467, max power of 3 before overflow
    return n > 0 and pow(3, int(math.log(1 << 31) / math.log(3))) % n == 0

class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    return n > 0 and pow(3, round(math.log(n) / math.log(3))) == n
