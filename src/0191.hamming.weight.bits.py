class Solution:
  def hammingWeight(self, n: int) -> int:
    """bit manipulation:
      n & (n - 1) mask the rightmost 1 into 0
      n & ~(n - 1) get out rigthmost 1 with trailing zeros, e.g., rightmost 1's index
    """
    ans = 0
    while n > 0:
      n &= (n - 1)
      ans += 1
    return ans