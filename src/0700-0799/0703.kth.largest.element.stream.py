import bisect

class KthLargest:

  def __init__(self, k: int, nums: List[int]):
    self.nums = sorted([-x for x in nums])[:k]
    self.size = k

  def add(self, val: int) -> int:
    i = bisect.bisect_right(self.nums, -val)
    if i < self.size:
      self.nums.insert(i, -val)
      if len(self.nums) > self.size:
        self.nums.pop() 
    return -self.nums[-1]
