from typing import List

class Solution:
  def minDifference(self, nums: List[int]) -> int:
    nums.sort()
    return min(x - y for x, y in zip(nums[-4:], nums[:4])) if len(nums) > 4 else 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.minDifference(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
