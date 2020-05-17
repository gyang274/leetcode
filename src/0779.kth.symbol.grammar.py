class Solution:
  def kthGrammar(self, N: int, K: int) -> int:
    """K -= 1 makes K 0-indexed rather than 1-indexed.
      k is determined by k // 2, or say, k determines 2k and 2k + 1
      k == 0, (2k, 2k + 1) is (0, 1)
      k == 1, (2k, 2k + 1) is (1, 0)
      so k ^ 2k == 1 and k ^ (2k + 1) == 0
    """
    K -= 1
    b = 0
    while K > 0:
      b ^= K % 2
      K //= 2
    return b

class Solution:
  def kthGrammar(self, N: int, K: int) -> int:
    """K -= 1 makes K 0-indexed rather than 1-indexed.
      k is determined by k // 2, or say, k determines 2k and 2k + 1
      k == 0, (2k, 2k + 1) is (0, 1)
      k == 1, (2k, 2k + 1) is (1, 0)
      so k ^ 2k == 1 and k ^ (2k + 1) == 0
    """
    K -= 1
    count = 0
    while K > 0:
      count += K % 2
      K //= 2
    return count & 1

class Solution:
  def kthGrammar(self, N: int, K: int) -> int:
    return bin(K - 1).count('1') & 1
