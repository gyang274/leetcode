class Solution:
  def _getGCD(self, x, y):
    while y:
      x, y = y, x % y
    return x
  def canMeasureWater(self, x: int, y: int, z: int) -> bool:
    """canMeasure if and only if z % gcd(x, y) == 0
    """
    return (z == 0) or (0 < z <= x + y and z % self._getGCD(x, y) == 0)