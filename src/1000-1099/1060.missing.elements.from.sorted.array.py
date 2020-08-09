from typing import List

class Solution:
  def missingElement(self, nums: List[int], k: int) -> int:
    n = len(nums)
    # # z: num of missing over array
    # z = nums[-1] - nums[0] + 1 - n
    # if k > z:
    #   return nums[-1] + (k - z)
    # z: num of missing at any index
    z = lambda i: (nums[i] - nums[0]) - i
    # binary search O(logN)
    l, r = 0, n - 1
    while l < r:
      m = r - (r - l) // 2
      if k <= z(m):
        r = m - 1
      else:
        l = m
    return nums[l] + k - z(l)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,4], 2),
    ([4,7,9,10], 1),
    ([4,7,9,10], 3),
  ]
  rslts = [solver.missingElement(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
