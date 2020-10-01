from typing import List
from collections import defaultdict, deque

import heapq

class Solution:
  def minJumps(self, arr: List[int]) -> int:
    n = len(arr)
    # priority queue, O(NlogN)
    d = defaultdict(set)
    for i, x in enumerate(arr):
      d[x].add(i)
    q, s = [(0, 0)], defaultdict(lambda: float('inf'))
    s[0] = 0
    while q:
      m, i = heapq.heappop(q)
      i = -i
      if i - 1 >= 0 and s[i - 1] > m + 1:
        s[i - 1] = m + 1
        heapq.heappush(q, (m + 1, -(i - 1)))
      if i + 1 < n and s[i + 1] > m + 1:
        if i + 1 == n - 1:
          return m + 1
        s[i + 1] = m + 1
        heapq.heappush(q, (m + 1, -(i + 1)))
      x, js = arr[i], set()
      for j in d[x]:
        if s[j] > m + 1:
          if j == n - 1:
            return m + 1
          s[j] = m + 1
          heapq.heappush(q, (m + 1, -j))
        else:
          js.add(j)
      for j in js:
        d[x].remove(j)
    return s[n - 1]

class Solution:
  def minJumps(self, arr: List[int]) -> int:
    # graph, bfs, O(V+E)
    n = len(arr)
    if n == 1:
      return 0
    d = defaultdict(set)
    for i, x in enumerate(arr):
      d[x].add(i)
    # bfs
    q, seen = [(0, 0)], {0}
    for i, s in q:
      if arr[i] in d:
        for j in d[arr[i]]:
          if j == n - 1:
            return s + 1
          if j not in seen:
            seen.add(j)
            q.append((j, s + 1))
        # key: no duplicate propagation. 
        d.pop(arr[i])
      for j in [i - 1, i + 1]:
        if 0 <= j < n and j not in seen:
          if j == n - 1:
            return s + 1
          seen.add(j)
          q.append((j, s + 1))
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
    [25,-28,-51,61,-74,-51,-30,58,36,68,-80,-64,25,-30,-53,36,-74,61,-100,-30,-52],
  ]
  rslts = [solver.minJumps(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
