from typing import List
from collections import defaultdict

class Solution:
  def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
    """TC: O(N + E), SC: O(N + E), Q0785.
    """
    # graph of dislike connections
    graph = defaultdict(set)
    for u, v in dislikes:
      graph[u].add(v)
      graph[v].add(u)
    # s: side of node i, s[i] = 0 or 1.
    s = {}
    for i in range(N):
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
    (3, [[1,2],[1,3],[2,3]]),
    (4, [[1,2],[1,3],[2,4]]),
    (5, [[1,2],[2,3],[3,4],[4,5],[1,5]]),
  ]
  rslts = [solver.possibleBipartition(N, dislikes) for N, dislikes in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")