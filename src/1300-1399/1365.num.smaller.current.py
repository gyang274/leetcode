from typing import List
from collections import defaultdict

class Solution:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    d = defaultdict(list)
    for i, x in enumerate(nums):
      d[x].append(i)
    ans = [None] * (len(nums))
    val = 0
    for x in sorted(d.keys()):
      for i in d[x]:
        ans[i] = val
      val += len(d[x])
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.smallerNumbersThanCurrent(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
