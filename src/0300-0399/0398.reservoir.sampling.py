import random

class Solution:
  # think the nums as a infinity data stream with random stoppage time..
  def __init__(self, nums: List[int]):
    self.nums = nums
  def pick(self, target: int) -> int:
    r, count = None, 0
    for i, x in enumerate(self.nums):
      if x == target:
        if random.randint(0, count) == 0:
          r = i
        count += 1
    return r
