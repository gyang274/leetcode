class Solution:
  def isPrime(self, x: int) -> bool:
    return x > 1 and all(x % d for d in range(2, int(x ** 0.5) + 1))
  def _getGCD(self, x: int, y: int) -> int:
    while y:
      x, y = y, x % y
    return x  
  def _getLCM(self, x: int, y: int) -> int:
    return x * y // self._getGCD(x, y)