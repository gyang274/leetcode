import math

class Solution:
  def constructRectangle(self, area: int) -> List[int]:
    for x in range(math.ceil(math.sqrt(area)), area + 1):
      if area % x == 0:
        return [x, area // x]
