from collections import Counter

class FirstUnique:

  def __init__(self, nums: List[int]):
    self.nums = nums
    self.i = 0
    self.n = len(nums)
    self.d = Counter(nums)

  def showFirstUnique(self) -> int:
    # amortized O(1)
    while self.i < self.n and self.d[self.nums[self.i]] > 1:
      self.i += 1
    return -1 if self.i == self.n else self.nums[self.i]        

  def add(self, value: int) -> None:
    self.nums.append(value)
    self.n += 1
    self.d[value] += 1
