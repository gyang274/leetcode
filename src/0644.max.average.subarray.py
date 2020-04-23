from typing import List
from collections import deque

class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    """O(N): convex hull window.
      Kai-min Chung, Hsueh-I Lu - An Optimal Algorithm for the Maximum-Density Segment Problem. 2008.
    """
    n = len(nums)
    # nums to prefix sum, e.g.,
    # nums[i] = sum(nums[:i]), i = 0, .., n
    for i in range(1, n):
      nums[i] += nums[i - 1]
    nums.insert(0, 0)
    # d: density
    d = lambda i, j: (nums[j] - nums[i]) / (j - i)
    # q: queue (convex hull) of potential starting index, high density points
    q, xmax = deque([]), nums[n] // n
    for j in range(k, n + 1):
      # j - k will be available as a starting index
      # say, density(i, j - k - 1) >= density(j - k - 1, j - k), then should never include j - k - 1 by itself
      # instead, include either i -> j - k - 1 all together with j - k, or include j - k by itself
      # generally, this applies to density(i0, i1) >= density(i1, j - k), i0 < i1 < j - k
      while len(q) > 1 and d(q[-2], q[-1]) >= d(q[-1], j - k):
        q.pop()
      q.append(j - k)
      while len(q) > 1 and d(q[0], q[1]) <= d(q[1], j):
        q.popleft()
      xmax = max(xmax, d(q[0], j))
    return xmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,12,-5,-6,50,3], 4),
    ([1,1,1,1,1000,1000,0,0,0,0,0,1000,1000,1000], 4),
    ([1,1,1,1,1000,1000,0,0,0,0,0,1000,1000,1000,1000,1000], 4),
  ]
  rslts = [solver.findMaxAverage(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
