from typing import List
from collections import deque

class Solution:
  def numMovesStonesII(self, stones: List[int]) -> List[int]:
    # sort: O(NlogN)
    stones.sort()
    # xmin: slide window: O(N)
    n = len(stones)
    xmin, queue = n, deque([])
    for x in stones:
      while queue and queue[0] < x - (n - 1):
        queue.popleft()
      queue.append(x)
      if len(queue) == n - 1 and queue[0] > x - (n - 1):
        xmin = 2
      else:
        xmin = min(xmin, n - len(queue))
    # xmax: straightforward math: O(1)
    xmax = max((stones[-2] - stones[0]), (stones[-1] - stones[1])) - (n - 2)
    return xmin, xmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [3,2,1,0,4],
    [3,2,1,0,4,8],
  ]
  rslts = [solver.numMovesStonesII(stones) for stones in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
