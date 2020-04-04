# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
  def rand10(self) -> int:
    """(x1, x2), map 49 -> 10.
    """
    x = 42
    while x > 40:
      x = 1 + (rand7() - 1) + 7 * (rand7() - 1)
    return 1 + (x - 1) % 10

class Solution:
  def rand10(self) -> int:
    """(x1, x2, x3, x4), map 2401 -> 10, more efficient.
    """
    x = 2401
    while x > 2400:
      x = 1 + (rand7() - 1) + 7 * (rand7() - 1) + 49 * (rand7() - 1) + 343 * (rand7() - 1)
    return 1 + (x - 1) % 10

class Solution:
  def rand10(self) -> int:
    """(x1, x2), map 49 -> 10, reuse residual, step by step version of (x1, x2, x3, x4), map 2401 -> 10.
    """
    while True:
      x = 1 + (rand7() - 1) + 7 * (rand7() - 1)
      if x <= 40:
        return 1 + (x - 1) % 10
      # x: 41 - 49 -> 1 - 9 -> 1 - 63
      x = 1 + (rand7() - 1) + 7 * ((x % 10) - 1)
      if x <= 60:
        return 1 + (x - 1) % 10
      # x: 61 - 63 -> 1 - 3 -> 1 - 21
      x = 1 + (rand7() - 1) + 7 * ((x % 10) - 1)
      if x <= 20:
        return 1 + (x - 1) % 10
