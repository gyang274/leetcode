from typing import List
from collections import deque

class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    """Keep a queue of length k - 1, if nums keep going up then last one is running max, no need to use queue,
      if at anytime nums going down then push running max into queue and if going down again then push into queue again, 
      so queue is trending down with queue[0] be the max from backward window k, and at any index i only need to compare 
      queue[0] and nums[i], also when i - k == queue[0]'s index, pop it from queue. This is similar to Q0084 & Q0085.
      TC: O(N), SC: O(k), since each item is append and pop from queue at most once each operation.
    """
    if not nums:
      return nums 
    ans, queue = [], deque([]), 
    for i in range(k - 1):
      while queue and nums[i] >= queue[-1][1]:
        queue.pop()
      queue.append((i, nums[i]))
    for i in range(k - 1, len(nums)):
      if queue and queue[0][0] < i - k + 1:
        queue.popleft()
      while queue and nums[i] >= queue[-1][1]:
        queue.pop()
      queue.append((i, nums[i]))
      ans.append(queue[0][1])
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([], 0),
    ([1], 1),
    ([1,2,3,4,5,6,7,8], 3),
    ([8,7,6,5,4,3,2,1], 3),
    ([1,8,2,7,3,6,4,5], 3),
  ]
  rslts = [solver.maxSlidingWindow(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")