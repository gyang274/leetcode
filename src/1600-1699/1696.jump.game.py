from collections import deque

class Solution:
  def maxResult(self, nums: List[int], k: int) -> int:
    # stack, TC: O(N), SC: O(K)
    n = len(nums)
    # sliding window of size k, since k can be as large as 10^5, dp is ok but overkill
    # keep a stack of decreasing scores as the potential next maximum as the sliding window go through left to right
    s = deque([(nums[0], 0)])
    # score, save the score on the nums in-place
    for i in range(1, n):
      while i - s[0][1] > k:
        s.popleft()
      nums[i] += s[0][0]
      while s and nums[i] >= s[-1][0]:
        s.pop()
      s.append((nums[i], i))
    return nums[-1]