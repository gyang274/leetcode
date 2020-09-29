from typing import List

import heapq

class Solution:
  def maxJumps(self, arr: List[int], d: int) -> int:
    n = len(arr)
    # TC: O(NlogN + ND), SC: O(N)
    s = {}
    # priority queue
    q = [(x, i) for i, x in enumerate(arr)]
    heapq.heapify(q)
    while q:
      # x is the min of unvisited, max of the visited
      x, i = heapq.heappop(q)
      # init
      s[i] = 1
      # jump to i from left
      for k in range(i - 1, max(i - d - 1, -1), -1):
        if k in s and arr[k] < x:
          s[i] = max(s[i], s[k] + 1)
        else:
          break
      # jump to i from right
      for k in range(i + 1, min(i + d + 1,  n), +1):
        if k in s and arr[k] < x:
          s[i] = max(s[i], s[k] + 1)
        else:
          break
    return max(s.values())

class Solution:
  def maxJumps(self, arr: List[int], d: int) -> int:
    # stack, TC: O(N), SC: O(N).
    A, n = arr, len(arr)
    # stack is index with decreasing of values, pending jumpping from right, being popped when meet next wall on right.
    s, stack = [1] * (n + 1), []
    for i, x in enumerate(A + [float('inf')]):
      while stack and A[stack[-1]] < x:
        queue = [stack.pop()]
        while stack and A[stack[-1]] == A[queue[-1]]:
          queue.append(stack.pop())
        # j is min between stack[-1] and i, reverse jump up to stack[-1] and i
        for j in queue:
          if i - j <= d:
            s[i] = max(s[i], s[j] + 1)
          if stack and j - stack[-1] <= d:
            s[stack[-1]] = max(s[stack[-1]], s[j] + 1)
      stack.append(i)
    return max(s[:-1])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,4,5,6,7], 1),
    ([7,6,5,4,3,2,1], 1),
    ([2,7,1,4,2,7,1,4,7], 2),
    ([6,4,14,6,8,13,9,7,10,6,12], 2),
  ]
  rslts = [solver.maxJumps(arr, d) for arr, d in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
