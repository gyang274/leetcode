from typing import List
from collections import Counter

class Solution:
  def isPossibleDivide(self, nums: List[int], k: int) -> bool:
    d, s = Counter(nums), sorted(set(nums))
    for x in s:
      if d[x]:
        m = d[x]
        for i in range(k):
          d[x + i] -= m
          if d[x + i] < 0:
            return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,4], 2),
    ([1,2,3,4], 3),
    ([3,3,2,2,1,1], 3),
    ([1,2,3,3,4,4,5,6], 4),
    ([3,2,1,2,3,4,3,4,5,9,10,11], 3)
  ]
  rslts = [solver.isPossibleDivide(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
