class Solution:
  def isOneBitCharacter(self, bits: List[int]) -> bool:
    n = len(bits)
    if n == 1:
      return True
    i = n - 2
    while i >= 0 and bits[i] == 1:
      i -= 1
    return not ((n - i) & 1)
