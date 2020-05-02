class Solution:
  def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r:
      m = l + (r - l) // 2
      if nums[m] == target:
        return m
      elif nums[m] > target:
        r = m
      else:
        l = m + 1
    return -1
        