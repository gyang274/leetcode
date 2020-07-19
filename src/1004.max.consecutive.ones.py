from typing import List
from collections import deque

class Solution:
  def longestOnes(self, A: List[int], K: int) -> int:
    # Q0485, Q0487, O(NK)
    # n[i]: num of consecutive ones by flipping i 0s.
    n, m = [0] * (K + 1)
    for x in A:
      if x:
        n = list(map(lambda z: z + 1, n))
      else:
        n = [0] + list(map(lambda z: z + 1, n[:-1]))
      m = list(map(max, zip(m, n)))
    return max(m)

class Solution:
  def longestOnes(self, A: List[int], K: int) -> int:
    # Q0485, Q0487, O(N)
    queue, nx, mx = deque([0]), 0, 0
    for x in A:
      queue[0] += 1
      if not x:
        if len(queue) == K + 1:
          nx -= queue.pop()
        queue.appendleft(0)
      nx += 1
      mx = max(mx, nx)
    return mx

class Solution:
  def longestOnes(self, A: List[int], K: int) -> int:
    # Q0485, Q0487, O(N), sliding window
    i = 0
    for j in range(len(A)):
      K -= 1 - A[j]
      if K < 0:
        K += 1 - A[i]
        i += 1
    return j - i + 1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,1,1,0,0,0,1,1,1,1,0], 2),
    ([1,1,1,0,0,1,1,1,1,0,0,0,0,0,0], 2),
    ([1,0,1,0,0,1,0,0,1,1,0,1,1,1,0,0,0], 2),
    ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3),
  ]
  rslts = [solver.longestOnes(A, K) for A, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
