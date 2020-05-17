class Solution:
  def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
    """O(log(max(tx, ty))), walk backward.
      forward: (x, y) -> (x, x + y) and (x + y, y), 1p2c like in binary tree
      ---
      x, y -> (x, y)
      x, x + y, y -> (x, x + y), (x + y, y)
      x, 2x + y, x + y, x + 2y, y -> (x, 2x + y), (2x + y, x + y), (x + y, x + 2y), (x + 2y, y)
      ...
      backward: (x, y) -> (x - y, y) if x > y else (x, y - x), x, y > 0, every children has one and only one parent!
      aggressively, (x, y) -> (x % y, y) if x > y else (x, y % x)
    """
    while tx >= sx and ty >= sy:
      if tx == ty:
        break
      elif tx > ty:
        if ty > sy:
          tx %= ty
        else:
          return (tx - sx) % ty == 0
      else:
        if tx > sx:
          ty %= tx
        else:
          return (ty - sy) % tx == 0
    return (tx, ty) == (sx, sy)
