from typing import List

class Solution:
  def maxSubArrayLen(self, nums: List[int], k: int) -> int:
    """modified two sum over the partial sum of subarray.
    """
    if not nums: return 0
    # xsum: hashmap of s -> i
    # s: sum(nums[0..i]), where i is the smallest index s.t sum(nums[0..i]) == s
    xsum = {nums[0]: 0}
    for i in range(1, len(nums)):
      nums[i] += nums[i - 1]
      if nums[i] not in xsum:
        xsum[nums[i]] = i
    # if nums[(i+1)..j] == k then nums[0..j] - nums[0..i] = k => nums[0..j] - k = nums[0..i] for some i, length j - i
    xmax = 0
    for i, s in enumerate(nums):
      if s == k:
        xmax = max(xmax, i + 1)
      elif s - k in xsum:
        xmax = max(xmax, i - xsum[s - k])
    return xmax

class Solution:
  def maxSubArrayLen(self, nums: List[int], k: int) -> int:
    """modified two sum over the partial sum of subarray.
    """
    # xsum: hashmap of s -> i
    # s: sum(nums[0..i]), where i is the smallest index s.t sum(nums[0..i]) == s
    xmax, xsum, nums = 0, {0: 0}, [0] + nums
    for i in range(1, len(nums)):
      nums[i] += nums[i - 1]
      # update xsum
      if nums[i] not in xsum:
        xsum[nums[i]] = i
      # update xmax
      if nums[i] - k in xsum:
        xmax = max(xmax, i - xsum[nums[i] - k])
    return xmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([], 0),
    ([0], 0),
    ([-2, -1, 2, 1], 1),
    ([1, -1, 5, -2, 3], 3),
  ]
  rslts = [solver.maxSubArrayLen(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")