class Solution:
  def canWinNim(self, n: int) -> bool:
    """strategy: one move x the other move 4 - x, x = 1, 2, 3, so 1st can with if not n % 4 == 0.
    """
    return not n % 4 == 0