class Solution:
  def convertToBase7(self, num: int) -> str:
    if num == 0:
      return "0"
    s = "" if num > 0 else "-"
    x = ""
    z = abs(num)
    while z > 0:
      x = str(z % 7) + x
      z //= 7
    return s + x