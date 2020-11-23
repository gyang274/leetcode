from typing import List

class Solution:
  def maxNonOverlapping(self, nums: List[int], target: int) -> int:
    # TC: O(N), SC:O(N)
    n = len(nums)
    # prefix sum
    for i in range(1, n):
      nums[i] += nums[i - 1]
    seen, dp = {0: -1}, [0] * n
    for i in range(n):
      x = nums[i] - target
      if x in seen:
        dp[i] = max(dp[i - 1], dp[seen[x]] + 1)
      else:
        dp[i] = dp[i - 1]
      seen[nums[i]] = i
    return dp[-1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([0,0,0], 0),
    ([1,1,1,1,1], 2),
    ([-1,3,5,1,4,2,-9], 6),
    ([-2,6,6,3,5,4,1,2,8], 10),
  ]
  rslts = [solver.maxNonOverlapping(nums, target) for nums, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
