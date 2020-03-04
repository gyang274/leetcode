class NumArray:
  def __init__(self, nums: List[int]):
    """store partial sum of 0-i for i<n, so any range sum is O(1).
    """
    self.nums = nums
    for i in range(1, len(self.nums)):
      self.nums[i] += self.nums[i - 1]
  def sumRange(self, i: int, j: int) -> int:
    return self.nums[j] - (self.nums[i - 1] if i > 0 else 0)