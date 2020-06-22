from typing import List
from collections import defaultdict, deque

class Solution:
  def shortestPathLength(self, graph: List[List[int]]) -> int:
    """TC: O(N*2^N).
    """
    # bfs
    n = len(graph)
    # init queue with start at each node, use the binary bits of cover represents visited nodes
    queue = deque((1 << i, i) for i in range(n))
    # dist
    dist = defaultdict(lambda: n * n)
    for i in range(n):
      dist[(1 << i, i)] = 0
    # main
    while queue:
      cover, head = queue.popleft()
      d = dist[(cover, head)]
      if cover == ((1 << n) - 1):
        return d
      for i in graph[head]:
        cnext = cover | (1 << i)
        if d + 1 < dist[(cnext, i)]:
          dist[(cnext, i)] = d + 1
          queue.append((cnext, i))

class Solution:
  def shortestPathLength(self, graph: List[List[int]]) -> int:
    """TC: O(N*2^N).
    """
    # dynamic programming
    n = len(graph)
    # dist of (head, cover)
    dist = [[float('inf')] * n for i in range(1 << n)]
    for i in range(n):
      dist[1 << i][i] = 0
    # main
    for cover in range(1 << n):
      repeat = True
      while repeat:
        repeat = False
        for head, d in enumerate(dist[cover]):
          for i in graph[head]:
            cnext = cover | (1 << i)
            if d + 1 < dist[cnext][i]:
              dist[cnext][i] = d + 1
              if cnext == cover:
                repeat = True
    return min(dist[(1 << n) - 1])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2,3],[0],[0],[0]],
    [[1],[0,2,4],[1,3,4],[2],[1,2]],
  ]
  rslts = [solver.shortestPathLength(graph) for graph in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
