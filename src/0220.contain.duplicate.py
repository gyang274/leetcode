from typing import List

class Solution:
  def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    """hash table sliding window size k + buckets.
    """
    n = len(nums)
    if n < 2:
      return False
    if t < 0:
      return False
    xmin, xmax = min(nums), max(nums)
    # bucket of [xmin + i * (t + 1), xmin + (i + 1) * (t + 1)), i = 0, 1, ..
    # buckets = [None for i in range(xmin, xmax + 1, t + 1)]
    # nb = len(buckets)
    # ^ memory limit exceed ([2147483647, -2147483645], 1, 5)
    # improvement: no need to allocate the buckets beforehand, use i of xmin + i * (t + 1) as key
    buckets = {}
    # go through nums, each bucket at most one, each nums just need to consider adjacent buckets
    for i in range(n):
      if i > k:
        buckets.pop((nums[i - k - 1] - xmin) // (t + 1))
      b = (nums[i] - xmin) // (t + 1)
      if b in buckets:
        return True
      if b - 1 in buckets and nums[i] - buckets[b - 1] <= t:
        return True
      if b + 1 in buckets and buckets[b + 1] - nums[i] <= t:
        return True
      buckets[b] = nums[i]
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,5,9,1,5,9],2,3),
  ]
  rslts = [solver.containsNearbyAlmostDuplicate(nums, k, t) for nums, k, t in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")