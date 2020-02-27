class Solution:
  def addDigits(self, num: int) -> int:
    """The mapping is \sum_{i} a_i * (10 * i) -> \sum_{i} a_i, so num -> num % 9
    """
    return 0 if num == 0 else (9 if num % 9 == 0 else num % 9)
        