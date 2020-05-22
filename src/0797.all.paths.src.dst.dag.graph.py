from typing import List

class Solution:
  def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    r, q, n = [], [[0]], len(graph)
    while q:
      p = q.pop()
      if graph[p[-1]]:
        for i in graph[p[-1]]:
          if i == n - 1:
            r.append(p + [i])
          else:
            q.append(p + [i])
    return r

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2], [3], [3], []] ,
  ]
  rslts = [solver.allPathsSourceTarget(graph) for graph in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
