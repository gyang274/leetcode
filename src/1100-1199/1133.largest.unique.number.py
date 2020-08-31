from typing import List
from collections import Counter, defaultdict

class Solution:
  def largestUniqueNumber(self, A: List[int]) -> int:
    c, d = Counter(A), defaultdict(set)
    for k in c:
      d[c[k]].add(k)
    return max(d[1]) if 1 in d else -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [2,2,3,3,4,4,2],
    [5,7,3,9,4,9,8,3,1],
  ]
  rslts = [solver.largestUniqueNumber(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
