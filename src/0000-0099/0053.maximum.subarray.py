from typing import List


class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    """dynamic programming.
    """
    dp = [-2147483648 for _ in range(len(nums) + 1)] 
    for i in range(len(nums)):
      dp[i + 1] = max(dp[i] + nums[i], nums[i])
    return max(dp)


class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    """dynamic programming, with O(1) space.
    """
    # xsum: current subarray sum, xmax: current maximum subarray sum
    xsum, xmax = -2147483648, -2147483648
    for i in range(len(nums)):
      xsum = max(xsum + nums[i], nums[i])
      xmax = max(xmax, xsum)
    return xmax


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [],
    [1],
    [-1],
    [1, -1, 2],
    [1, -2, 2],
    [2, -1, 2],
    [-2,1,-3,4,-1,2,1,-5,4],
  ]
  rslts = [solver.maxSubArray(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")