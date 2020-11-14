class Solution:
  def threeConsecutiveOdds(self, nums: List[int]) -> bool:
    n = len(nums)
    if n < 3:
      return False
    nums = [x & 1 for x in nums]
    s = sum(nums[:3])
    if s == 3:
      return True
    for i in range(3, n):
      s += nums[i] - nums[i - 3]
      if s == 3:
        return True
    return False