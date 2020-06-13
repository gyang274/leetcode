from typing import List

class Solution:
  def minEatingSpeed(self, piles: List[int], H: int) -> int:
    if H == len(piles):
      return max(piles)
    l, r = max(1, sum(piles) // H), max(piles)
    while l < r:
      m = l + (r - l) // 2
      # s = sum(map(lambda x: (x // m) + bool(x % m), piles))
      s = sum(map(lambda x: (x - 1) // m + 1, piles))
      if s <= H:
        r = m
      else:
        l = m + 1
    return l

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([3,6,7,11], 8),
    ([30,11,23,4,20], 5),
    ([30,11,23,4,20], 6), 
  ]
  rslts = [solver.minEatingSpeed(piles, H) for piles, H in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
