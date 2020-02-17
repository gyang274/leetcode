from typing import List

class Solution:
  def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    """Two pointers, i <= j, keep track j - i.
      move j forward until nums[i:j] >= s, then move i forward until nums[i:j] < s, .. until j reach the ende.
      O(n) as at most 2 * len(nums) since i and j move forward only so each node can be visited at most twice.
    """
    if sum(nums) < s:
      return 0
    i, j, n = 0, 1, len(nums)
    xmin, xsum = n, nums[0]
    while j < n or xsum >= s:
      while j < n and xsum < s:
        j += 1
        xsum += nums[j - 1]
      xmin = min(j - i, xmin)
      i += 1
      xsum -= nums[i - 1]
    return xmin

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, [1,1,1,1]),
    (7, [2,3,1,2,4,3]),
    (213, [12,28,83,4,25,26,25,2,25,25,25,12]),
  ]
  rslts = [solver.minSubArrayLen(s, nums) for s, nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}") 