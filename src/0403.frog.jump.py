from typing import List
from collections import defaultdict

import heapq

class Solution:
  def canCross(self, stones: List[int]) -> bool:
    """dynamic programming: O(N^2)
      dp[n][k] = True/False, can jump to stone at position n with a step k, 
      dp[n][k] = dp[n - k][k - 1] or dp[n - k][k] or dp[n - k][k + 1]
    """
    n = stones[-1]
    dp = [[False] * (n + 2) for _ in range(n + 1)]
    dp[0][0] = True
    for i in stones[1:]:
      for k in range(1, i + 1):
        dp[i][k] = dp[i - k][k - 1] or dp[i - k][k] or dp[i - k][k + 1]
    return any(dp[n])

class Solution:
  def canCross(self, stones: List[int]) -> bool:
    """dynamic programming: O(N^2)
      dp[n][k] = True/False, can jump to stone at position n with a step k, 
      dp[n][k] = dp[n - k][k - 1] or dp[n - k][k] or dp[n - k][k + 1]
    """
    n = stones[-1]
    dp = [[False] * (n + 2) for _ in range(n + 1)]
    dp[0][0] = True
    for i in stones[1:]:
      for j in stones[:i]:
        # jump from stone j to i with step k = i - j
        dp[i][i - j] = dp[j][i - j - 1] or dp[j][i - j] or dp[j][i - j + 1]
    return any(dp[n])

class Solution:
  def canCross(self, stones: List[int]) -> bool:
    """dynamic programming: O(N^2)
      dp[i][j] = True/False, can jump from stone at position j to stone at position i, 
        if can jump from stone at position j - (i - j) [+-0/1] to stone at position j.
      dp[i][j] = dp[j][j - ((i - j) - 1)] or dp[j][j - (i - j)] or dp[j][j - ((i - j) + 1)]
    """
    n = len(stones)
    dp = defaultdict(set)
    dp[0] = {0}
    for i in range(n):
      for j in range(i):
        si, sj = stones[i], stones[j]
        if {sj - ((si - sj) - 1), sj - (si - sj), sj - ((si - sj) + 1)} & dp[sj]:
          dp[si].add(sj)
    return len(dp[stones[-1]]) > 0

class Solution:
  def canCross(self, stones: List[int]) -> bool:
    """dynamic programming + priority queue with BFS
    """
    # init queue with jump from 0 to 0 with step 0
    q, s, d, v = [(0, 0), ], set(stones), stones[-1], set([(0, 0), ])
    while q:
      i, k = heapq.heappop(q)
      if d in {i + k - 1, i + k, i + k + 1}:
        return True
      if k > 1 and i + k - 1 in s:
        if (i + k - 1, k - 1) not in v:
          v.add((i + k - 1, k - 1))
          heapq.heappush(q, (i + k - 1, k - 1))
      if k > 0 and i + k in s:
        if (i + k, k) not in v:
          v.add((i + k, k))
          heapq.heappush(q, (i + k, k))
      if i + k + 1 in s:
        if (i + k + 1, k + 1) not in v:
          v.add((i + k + 1, k + 1))
          heapq.heappush(q, (i + k + 1, k + 1))
    return False

class Solution:
  def canCross(self, stones: List[int]) -> bool:
    """dynamic programming + priority queue with DFS
    """
    # init queue with jump from 0 to 0 with step 0
    q, s, d, v = [(0, 0), ], set(stones), stones[-1], set([(0, 0), ])
    while q:
      i, k = heapq.heappop(q)
      i, k = -i, -k
      if d in {i + k - 1, i + k, i + k + 1}:
        return True
      if k > 1 and i + k - 1 in s:
        if (i + k - 1, k - 1) not in v:
          v.add((i + k - 1, k - 1))
          heapq.heappush(q, (-(i + k - 1), -(k - 1)))
      if k > 0 and i + k in s:
        if (i + k, k) not in v:
          v.add((i + k, k))
          heapq.heappush(q, (-(i + k), -k))
      if i + k + 1 in s:
        if (i + k + 1, k + 1) not in v:
          v.add((i + k + 1, k + 1))
          heapq.heappush(q, (-(i + k + 1), -(k + 1)))
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0,1],
    [0,2],
    [0,2147483647],
    [0,1,3,5,6,8,12,17],
    [0,1,2,3,4,8,9,11,14],
    [i for i in range(1000)],
  ]
  rslts = [solver.canCross(stones) for stones in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
