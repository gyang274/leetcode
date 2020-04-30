class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    n = len(nums)
    x = xmax = sum(nums[:k]) / k
    for i in range(k, n):
      x += (nums[i] - nums[i - k]) / k
      xmax = max(xmax, x)
    return xmax
