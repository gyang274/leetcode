from typing import List

class Solution:
  def isBipartite(self, graph: List[List[int]]) -> bool:
    """dfs modified
    """
    n = len(graph)
    # s: side of node i, s[i] = 0 or 1.
    s = {}
    for i in range(n):
      if i not in s:
        s[i] = 0
        # dfs
        stack = [i]
        while stack:
          j = stack.pop()
          for k in graph[j]:
            if k in s:
              if s[j] == s[k]:
                return False
            else:
              s[k] = s[j] ^ 1
              stack.append(k)
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1],[0,3],[3],[1,2]],
    [[1],[0],[4],[4],[2,3]],
    [[4],[],[4],[4],[0,2,3]],
    [[1,3],[0,2],[1,3],[0,2]],
    [[3],[2,4],[1],[0,4],[1,3]],
    [[1,2,3],[0,2],[0,1,3],[0,2]],
  ]
  rslts = [solver.isBipartite(graph) for graph in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
