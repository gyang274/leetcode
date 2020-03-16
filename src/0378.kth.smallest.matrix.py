from typing import List

import heapq

class Solution:
  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    """Q0373, priority queue + dynamic boundary explore (BFS).
    """
    # 1 ≤ k ≤ n2, so..
    n = len(matrix)
    # build the priority queue key by matrix[i][j]
    visited, q, x = set([(0, 0), ]), [(matrix[0][0], 0, 0), ], []
    # heapq.heapify(q)
    # add one at a time
    while len(x) < k:
      _, i, j = heapq.heappop(q)
      if i + 1 < n and (i + 1, j) not in visited:
        heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
        visited.add((i + 1, j))
      if j + 1 < n and (i, j + 1) not in visited:
        heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        visited.add((i, j + 1))
      x.append(matrix[i][j])
    return x[-1]

class Solution:
  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    # init q with min(k, n) row's smallest element
    # and then move w.r.t boundary at each row.
    q = []
    for i in range(min(k, n)):
      heapq.heappush(q, (matrix[i][0], i, 0))
    for _ in range(k):
      x, i, j = heapq.heappop(q)
      if j + 1 < n:
        heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
    return x

# NOTE: http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf, O(n), or say, O(min(n, k, n^2 - k)).

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([
      [ 1,  5,  9],
      [10, 11, 13],
      [12, 13, 15]
    ], 8),
  ]
  rslts = [solver.kthSmallest(matrix, k) for matrix, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")