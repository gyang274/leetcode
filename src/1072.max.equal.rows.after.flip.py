from typing import List
from collections import Counter

class Solution:
  def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
    # only rows exact same or complementary are flip into same
    # flip 1st to 0 to so that only rows exact same are all same
    d = Counter()
    for row in matrix:
      if row[0] == 0:
        d[tuple(row)] += 1
      else:
        d[tuple(x ^ 1 for x in row)] += 1
    return max(d[k] for k in d)

class Solution:
  def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
    # only rows exact same or complementary are flip into same
    # flip 1st to 0 to so that only rows exact same are all same
    return max(Counter(tuple(x ^ 1 for x in r) if r[0] else tuple(r) for r in matrix).values())

class Solution:
  def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
    # only rows exact same or complementary are flip into same
    # flip 1st to 1 to so that only rows exact same are all same
    return max(Counter(tuple(x ^ r[0] for x in r) for r in matrix).values())

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,1],[1,1]],
    [[0,1],[1,0]],
    [[0,0,0],[0,0,1],[1,1,0]],
  ]
  rslts = [solver.maxEqualRowsAfterFlips(matrix) for matrix in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
