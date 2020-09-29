from typing import List

class Solution:
  def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    # Floyd-Warshall Algorithm, TC: O(N^3), SC: O(N^2).
    # dist[i][j] = min(dist[i][k] + dist[k][j], all k).
    dist = [[float('inf')] * n for _ in range(n)]
    # init
    for i, j, w in edges:
      dist[i][j] = dist[j][i] = w
    for i in range(n):
      dist[i][i] = 0
    # main
    for k in range(n):
      for i in range(n):
        for j in range(n):
          dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    ans = {sum(d <= distanceThreshold for d in dist[i]): i for i in range(n)}
    return ans[min(ans)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4),
    (5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2),
  ]
  rslts = [solver.findTheCity(n, edges, distanceThreshold) for n, edges, distanceThreshold in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
