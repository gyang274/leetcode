from typing import List
from collections import Counter

class Solution:
  def isNStraightHand(self, hand: List[int], W: int) -> bool:
    n = len(hand)
    if n % W:
      return False
    d, k = Counter(hand), n // W
    for _ in range(k):
      x = min(d.keys())
      for _ in range(W):
        if x in d:
          d[x] -= 1
          if d[x] == 0:
            d.pop(x)
          x += 1
        else:
          return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,6,2,3,4,7,8], 3),
    ([1,2,3,4,5], 4),
  ]
  rslts = [solver.isNStraightHand(hand, W) for hand, W in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
