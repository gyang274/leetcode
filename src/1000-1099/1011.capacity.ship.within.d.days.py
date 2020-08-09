from typing import List

class Solution:
  def shipWithinDays(self, weights: List[int], D: int) -> int:
    # simulate one loading in O(N)
    def numDays(x):
      days, load = 1, 0
      for w in weights:
        if load + w <= x:
          load += w
        else:
          load = w
          days += 1
      return days
    # binary search, O(NlogN)
    l, r = max(weights), sum(weights)
    while l < r:
      m = l + (r - l) // 2
      if numDays(m) <= D:
        r = m
      else:
        l = m + 1
    return l

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], 3),
    ([1,2,3,4,5,6,7,8,9,10], 5),
  ]
  rslts = [solver.shipWithinDays(weights, D) for weights, D in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
