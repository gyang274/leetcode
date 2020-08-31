from typing import List
from collections import Counter

class Solution:
  def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    return sum(map(lambda x: x * (x - 1) // 2, Counter(map(lambda x: (x[0], x[1]) if x[0] < x[1] else (x[1], x[0]), dominoes)).values()))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2],[2,1],[3,4],[5,6]],
  ]
  rslts = [solver.numEquivDominoPairs(dominoes) for dominoes in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
