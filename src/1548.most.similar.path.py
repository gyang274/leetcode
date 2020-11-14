from typing import List

class Solution:
  def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
    # dp[i][v]: smallest edit distance of length i ending city v.
    # dp[i][v] = min(dp[i - 1][u]) + cost(v) for all city u connect to v.
    # graph
    graph = [[] for _ in range(n)]
    for u, v in roads:
      graph[u].append(v)
      graph[v].append(u)
    # dp init
    m = len(targetPath)
    dp = [[m] * n for _ in range(m)]
    pr = [[0] * n for _ in range(m)]
    # dp main
    for v in range(n):
      dp[0][v] = 0 if names[v] == targetPath[0] else 1
    for i in range(1, m):
      for v in range(n):
        for u in graph[v]:
          if dp[i - 1][u] < dp[i][v]:
            dp[i][v] = dp[i - 1][u]
            pr[i][v] = u
        dp[i][v] += 0 if names[v] == targetPath[i] else 1
    # reconstruct the path
    path, dist = [0], m
    for v in range(n):
      if dp[-1][v] < dist:
        dist = dp[-1][v]
        path[0] = v
    for i in range(m - 1, 0, -1):
      u = pr[i][path[-1]]
      path.append(u)
    return path[::-1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (5, [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], ["ATL","PEK","LAX","DXB","HND"], ["ATL","DXB","HND","LAX"]),
    (4, [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]], ["ATL","PEK","LAX","DXB"], ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]),
    (6, [[0,1],[1,2],[2,3],[3,4],[4,5]], ["ATL","PEK","LAX","ATL","DXB","HND"], ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]),
  ]
  rslts = [solver.mostSimilar(n, roads, names, targetPath) for n, roads, names, targetPath in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
