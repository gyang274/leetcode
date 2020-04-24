class Solution:
  def newInteger(self, n: int) -> int:
    # n in base 9
    m, i = 0, 0
    while n > 0:
      m += (n % 9) * (10 ** i)
      n //= 9
      i += 1
    return m

class Solution(object):
  def newInteger(self, n):
    m = ''
    while n:
      m = str(n % 9) + m
      n //= 9
    return int(m)