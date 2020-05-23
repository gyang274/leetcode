from typing import List

class Solution:
  def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    i, j, count, p, n = 0, 0, 0, 1, len(nums)
    while i < n:
      while j < n and p * nums[j] < k:
        p *= nums[j]
        j += 1
      count += j - i
      if j > i:
        p /= nums[i]
      i += 1
      if j < i:
        j = i
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,4,5], 0),
    ([1,2,3,4,5], 4),
    ([2,3,1,1,4], 8),
  ]
  rslts = [solver.numSubarrayProductLessThanK(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")