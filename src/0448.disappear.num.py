from typing import List

class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    """Q0442, use the array index itself indicates a num seen or not.
    """
    for x in nums:
      if nums[abs(x) - 1] > 0:
        nums[abs(x) - 1] *= -1
    ans = []
    for i, x in enumerate(nums):
      if x > 0:
        ans.append(i + 1)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [1],
    [1,1],
    [1,1,2,2,3,4,5],
    [4,3,2,7,8,2,3,1],
  ]
  rslts = [solver.findDisappearedNumbers(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")