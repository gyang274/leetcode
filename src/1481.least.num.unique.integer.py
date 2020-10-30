from typing import List
from collections import Counter

class Solution:
  def findLeastNumOfUniqueInts(self, nums: List[int], k: int) -> int:
    xs, r = sorted(Counter(nums).values()), 0
    for x in xs:
      if k >= x:
        k -= x
        r += 1
      else:
        break
    return len(xs) - r

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], 2),
    ([3,2,1,0,4], 3),
  ]
  rslts = [solver.findLeastNumOfUniqueInts(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
