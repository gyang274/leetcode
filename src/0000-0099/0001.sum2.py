class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    ys = {}
    for i, x in enumerate(nums):
      if target - x not in ys:
        ys[x] = i
      else:
        return [ys[target - x], i]
