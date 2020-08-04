from typing import List

import bisect

class Solution:
  def validSubarrays(self, nums: List[int]) -> int:
    # O(NlogN)
    n = len(nums)
    # O(NlogN), sort
    xs = sorted([(x, i) for i, x in enumerate(nums)])
    # O(NlogN), count
    count, seen = 0, [n]
    for x, i in xs:
      k = bisect.bisect(seen, i)
      count += seen[k] - i
      seen.insert(k, i)
    return count

class Solution:
  def validSubarrays(self, nums: List[int]) -> int:
    # O(N), monotonic stack
    count, stack = 0, []
    for x in nums:
      while stack and stack[-1] > x:
        stack.pop()
      stack.append(x)
      count += len(stack)
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2,3],
    [2,2,2],
    [3,2,1],
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.validSubarrays(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
