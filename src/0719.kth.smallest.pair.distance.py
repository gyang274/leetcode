from typing import List

class Solution:
  def counter(self, d):
    # count num of pair distance <= d
    i, count = 0, 0
    for j, x in enumerate(self.nums):
      while self.nums[j] - self.nums[i] > d:
        i += 1
      count += j - i
    return count
  def smallestDistancePair(self, nums: List[int], k: int) -> int:
    """binary search over (0, max(nums) - min(nums))
    """
    self.nums = nums
    self.nums.sort()
    l, r = 0, self.nums[-1] - self.nums[0] + 1
    while l < r:
      m = l + (r - l) // 2
      if self.counter(m) >= k:
        r = m
      else:
        l = m + 1
    return l

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], 5),
  ]
  rslts = [solver.smallestDistancePair(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
