from typing import List
from collections import defaultdict

class Solution:
  def longestSubsequence(self, arr: List[int], difference: int) -> int:
    s, d = defaultdict(lambda: 0), difference
    for x in arr:
      s[x + d] = max(s[x + d], s[x] + 1)
    return max(s.values())

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], 1),
    ([2,3,1,1,4], 2),
    ([2,3,1,1,4], 3),
    ([2,3,1,1,4], 4),
    ([3,2,1,0,4], -1),
  ]
  rslts = [solver.longestSubsequence(arr, difference) for arr, difference in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
