class Solution:
  def flipLights(self, n: int, m: int) -> int:
    """math
      s1 1 1 1 1 1 1 1 .. 
      s2 1 0 1 0 1 0 1 ..
      s3 0 1 0 1 0 1 0 ..
      s4 1 0 0 1 0 0 1 ..
      s1-s4: switch num 1-4, 1/0 means applicable on light i
      note light 4 = light1 + light2 + light3, so only light 1-3 are independent, and 8 pattern in total
    """
    n = min(n, 3)
    if m == 0:
      return 1
    if m == 1:
      return [2, 3, 4][n - 1]
    if m == 2:
      return [2, 4, 7][n - 1]
    return [2, 4, 8][n - 1]
