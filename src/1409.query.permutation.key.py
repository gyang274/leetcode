from typing import List

class Solution:
  def processQueries(self, queries: List[int], m: int) -> List[int]:
    p, q = list(range(1, m + 1)), []
    for x in queries:
      i = p.index(x)
      q.append(i)
      p = [p[i]] + p[:i] + p[(i + 1):]
    return q

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], 5),
    ([3,2,1,5,4], 5),
  ]
  rslts = [solver.processQueries(queries, m) for queries, m in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
