class Solution:
  def divide(self, dividend: int, divisor: int) -> int:
    """
    Set quotient to 0
    Align leftmost digits in dividend and divisor
    Repeat
      If that portion of the dividend above the divisor is greater than or equal to the divisor
        Then subtract divisor from that portion of the dividend and concatentate 1 to the right hand end of the quotient
      Else concatentate 0 to the right hand end of the quotient
      Shift the divisor one place right
    Until dividend is less than the divisor
    Quotient is correct, dividend is remainder
    STOP
    """
    INT_MAX = 2 ** 31 - 1
    INT_MIN = - 2 ** 31
    if (dividend == INT_MIN):
      if (divisor ==  1):
        return INT_MIN
      elif (divisor == -1):
        return INT_MAX
      elif ((divisor & 1) == 1):
        return self.divide(dividend + 1, divisor)
      else:
        return self.divide(dividend >> 1, divisor >> 1)
    # sign
    sign = -1 if ((dividend > 0) ^ (divisor > 0)) else 1
    dividend = dividend if dividend > 0 else -dividend
    divisor = divisor if divisor > 0 else -divisor
    # dividend and divisor are positive
    z = 1
    while divisor <= dividend:
      divisor <<= 1
      z += 1
    quotient = 0
    while z > 0:
      # print(z, "{0:b}".format(dividend), "{0:b}".format(divisor), quotient)
      quotient <<= 1
      if dividend >= divisor:
        dividend -= divisor
        quotient += 1
      divisor >>= 1
      z -= 1
    return sign * quotient


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    (10, 3),
    (3, 10),
    (-2147483648, 1),
    (-2147483648, -1),
    (-2147483648, 2),
    (-2147483648, -2),
    (2147483647, 1),
    (2147483647, -1),
    (2147483647, 2),
    (2147483647, -2),
  ]
  rslts = [solver.divide(dividend, divisor) for dividend, divisor in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")