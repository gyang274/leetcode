from typing import List
from itertools import accumulate

import operator

class Solution:
  def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    x = list(accumulate(arr, operator.__xor__, initial = 0))
    return [x[i] ^ x[j + 1] for i, j in queries]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,5,8,23,42,85], [[0,1],[1,2],[0,2],[2,3],[0,3],[1,4],[3,5],[2,7]]),
  ]
  rslts = [solver.xorQueries(arr, queries) for arr, queries in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
