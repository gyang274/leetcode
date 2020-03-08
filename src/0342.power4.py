class Solution:
  def isPowerOfFour(self, num: int) -> bool:
    while num > 1:
      if num % 4 == 0:
        num //= 4
      else:
        return False
    return num == 1

class Solution:
  def isPowerOfFour(self, num: int) -> bool:
    return num > 0 and num & (num - 1) == 0 and num % 3 == 1

class Solution:
  def isPowerOfFour(self, num: int) -> bool:
    return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0
