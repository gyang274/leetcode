from typing import List
from collections import Counter

class Solution:
  def numIdenticalPairs(self, nums: List[int]) -> int:
    d = Counter(nums)
    return sum(d[x] * (d[x] - 1) // 2 for x in d)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.numIdenticalPairs(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
