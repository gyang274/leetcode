from typing import List
from collections import defaultdict

class Solution:
  def findJudge(self, N: int, trust: List[List[int]]) -> int:
    # indegree and outdegree, judge <=> indegree = N - 1, outdegree = 0
    di, do = defaultdict(set), defaultdict(set)
    for u, v in trust:
      di[v].add(u)
      do[u].add(v)
    for x in range(1, N + 1):
      if len(di[x]) == N - 1 and len(do[x]) == 0:
        return x
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, [[1,2],[2,3]]),
    (4, [[1,3],[1,4],[2,3],[2,4],[4,3]]),
  ]
  rslts = [solver.findJudge(N, trust) for N, trust in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
