class Solution:
  def hammingDistance(self, x: int, y: int) -> int:
    z = x ^ y
    count = 0
    while z:
      z &= z - 1
      count += 1
    return count