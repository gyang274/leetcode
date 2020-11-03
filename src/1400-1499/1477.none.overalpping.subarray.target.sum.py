from typing import List
from collections import deque
from itertools import accumulate

class Solution:
  def minSumOfLengths(self, arr: List[int], target: int) -> int:
    # TC: O(N), SC: O(N), prefix sum + deque
    x, n = list(accumulate(arr, initial=0)), len(arr)
    s, d = [], {}
    for i in range(n + 1):
      y = x[i] - target
      if y in d:
        s.append([i - d[y], d[y], i])
      d[x[i]] = i
    # min length beyond index i-th
    for k in range(len(s) - 2, -1, -1):
      s[k][0] = min(s[k][0], s[k + 1][0])
    ans, queue = float('inf'), deque([])
    for d, i, j in s:
      while queue and queue[0][-1] <= i:
        ans = min(ans, queue.popleft()[0] + d)
      queue.append((j - i, i, j))
    return ans if ans < float('inf') else -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([7,3,4,7], 7),
    ([4,3,2,6,2,3,5], 2),
    ([4,3,2,6,2,3,5], 3),
    ([4,3,2,6,2,3,5], 5),
    ([4,3,2,6,2,3,5], 8),
    ([4,3,2,6,2,3,5], 6),
    ([1,1,1,2,2,2,4,4], 6),
  ]
  rslts = [solver.minSumOfLengths(arr, target) for arr, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
