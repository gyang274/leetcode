from typing import List
from collections import deque

import bisect

class Solution:
  def maxWidthRamp(self, A: List[int]) -> int:
    """TC: O(NlogN), SC: O(N), maintain a stack of (x, i), x descrease while i increase.
    """
    # use deque (as reverse of stack) to accomodate bisect..
    stack, ans = deque([]), 0
    for i, x in enumerate(A):
      if stack and x >= stack[0][0]:
        k = bisect.bisect(stack, (x, i))
        ans = max(ans, i - stack[k - 1][1])
      else:
        stack.appendleft((x, i))
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [6,0,8,2,1,5],
    [9,8,1,0,1,9,4,0,4,1],
  ]
  rslts = [solver.maxWidthRamp(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
