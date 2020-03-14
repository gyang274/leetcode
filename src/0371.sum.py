class Solution:
  def getSum(self, a: int, b: int) -> int:
    # 32bits integer HEX
    MAX = 0x7FFFFFFF
    MIN = 0x80000000
    # 32bits all 1s
    mask = 0xFFFFFFFF
    # bit operation to simulate "+"
    while not b == 0:
      # use "& mask" to limit onto 32bits
      a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    # bit operation to simulate "unary -"
    return a if a <= MAX else ~(a ^ mask)