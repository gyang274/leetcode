class Solution:
  def maxProfit(self, inventory: List[int], orders: int) -> int:
    # x: inventory sorted, o: orders left, r: replica of max value balls, p: profit accumulated, 
    x, o, r, p = sorted(inventory + [0]), orders, 1, 0
    while o > 0:
      y, z = x.pop(), x[-1] if x else 0
      if y == z:
        pass
      elif (y - z) * r <= o:
        p += ((y + z + 1) * (y - (z + 1) + 1) // 2) * r
        o -= (y - z) * r
      else:
        q = o // r
        p += ((y + (y - q + 1)) * q // 2) * r
        o %= r
        p += (y - q) * o
        o = 0
      r += 1
    return p % (10 ** 9 + 7)
