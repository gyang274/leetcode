from typing import List

class Solution:
  def isArithmetics(self, x):
    n = len(x)
    # if n < 2:
    #   return False
    if n == 2:
      return True
    for i in range(2, n):
      if not x[i] - x[i - 1] == x[i - 1] - x[i - 2]:
        return False
    return True
  def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    return [self.isArithmetics(sorted(nums[i:(j + 1)])) for i, j in zip(l, r)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([4,6,5,9,3,7], [0,0,2], [2,3,5]),
  ]
  rslts = [solver.checkArithmeticSubarrays(nums, l, r) for nums, l, r in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
