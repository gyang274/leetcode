from typing import List

class Solution:
  def dist(self, si, sj, di, dj):
    """O(NM): BFS, A* search, Dijkstra's algorithm, Hadlock's algorithm.
    """
    if (si, sj) == (di, dj):
      return 0
    queue, visited, dist = set([(si, sj)]), set([(si, sj)]), 0
    while queue:
      qnext, dist = set([]), dist + 1
      for si, sj in queue:
        for mi, mj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
          ni, nj = si + mi, sj + mj
          if (ni, nj) == (di, dj):
            return dist
          if 0 <= ni < self.n and 0 <= nj < self.m and self.forest[ni][nj] > 0 and (ni, nj) not in visited:
            visited.add((ni, nj))
            qnext.add((ni, nj))
      queue = qnext
    return -1
  def cutOffTree(self, forest: List[List[int]]) -> int:
    # travel sequence O(NMlogNM)
    n, m = len(forest), len(forest[0])
    queue = [(-1, 0, 0)]
    for i in range(n):
      for j in range(m):
        if forest[i][j] > 1:
          queue.append((forest[i][j], i, j))
    queue.sort()
    # travel distance O((NM)^2)
    self.forest, self.n, self.m = forest, n, m
    cdist = 0
    for i in range(len(queue) - 1):
      dist = self.dist(*queue[i][1:], *queue[i + 1][1:])
      if dist == -1:
        return -1
      else:
        cdist += dist
    return cdist

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2,3],[0,0,4],[7,6,5]],
    [[1,2,3],[0,0,0],[7,6,5]],
    [[1,2,3],[0,0,0],[1,1,1]],
  ]
  rslts = [solver.cutOffTree(forest) for forest in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
