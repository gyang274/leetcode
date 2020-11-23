from typing import List

class Solution:
  def sumOddLengthSubarrays(self, nums: List[int]) -> int:
    n = len(nums)
    # consider how many times each index contributed to some subarray
    # at index i, nums[0]-nums[i], (i + 1) choices on left ended, nums[i]-nums[n-1], (n - i) choices on right ended,
    # so (i + 1) * (n - i) subarrays, and ((i + 1) * (n - i) // 2) + (n & 1 and (i & 1) ^ 1) subarrays with odd length, 
    # that contains nums[i]..
    return sum(x * ((i + 1) * (n - i) // 2) + (x if n & 1 and (i & 1) ^ 1 else 0) for i, x in enumerate(nums))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,4,2,5,3],
  ]
  rslts = [solver.sumOddLengthSubarrays(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
