class Solution:
  def pivotIndex(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
      return -1
    s = sum(nums)
    if s - nums[0] == 0:
      return 0
    for i in range(1, n):
      nums[i] += nums[i - 1]
      if s - nums[i] == nums[i - 1]:
        return i
    return -1
