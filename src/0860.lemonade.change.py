class Solution:
  def lemonadeChange(self, bills: List[int]) -> bool:
    d = {5: 0, 10: 0}
    for b in bills:
      if b == 5:
        d[5] += 1
      else:
        if b == 10:
          d[10] += 1
          d[5] -= 1
        else:
          if d[10] > 0:
            d[10] -= 1
          else:
            d[5] -= 2
          d[5] -= 1
        if d[5] < 0:
          return False
    return True