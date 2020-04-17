from typing import List

class Solution:
  def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    # convert nums to cumulative sums
    n = len(nums)
    for i in range(1, n):
      nums[i] += nums[i - 1]
    # hashmap r = sum(nums[:i]) % k -> i
    # sum(nums[i:j]) % k == 0 iff sum(nums[:i]) % k == 0 or sum(nums[:i]) % k = sum(nums[:j]) % k
    d = {}
    d[0] = -1
    for i in range(n):
      r = nums[i]
      if not k == 0:
        r %= k
      if r in d:
        if i - d[r] > 1:
          return True
      else:
        d[r] = i
    return False

class Solution:
  def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    # d: hashmap r = sum(nums[:i]) % k -> i
    # sum(nums[i:j]) % k == 0 iff sum(nums[:i]) % k == 0 or sum(nums[:i]) % k = sum(nums[:j]) % k
    d, r, n = {}, 0, len(nums)
    d[0] = -1
    for i in range(n):
      r += nums[i]
      if not k == 0:
        r %= k
      if r in d:
        if i - d[r] > 1:
          return True
      else:
        d[r] = i
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([0,0], 0),
    ([0,1], 0),
    ([0,1], 1),
    ([2,3,1,1,4], 7),
  ]
  rslts = [solver.checkSubarraySum(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
