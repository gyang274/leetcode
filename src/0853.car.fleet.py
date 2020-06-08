from typing import List

class Solution:
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)
    cp, cs, count = target, -1, 0
    for p, s in cars:
      if (target - p) / s > (target - cp) / cs:
        count += 1
        cp, cs = p, s
    return count