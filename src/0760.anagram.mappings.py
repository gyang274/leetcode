from typing import List
from collections import defaultdict

class Solution:
  def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
    d = defaultdict(set)
    for i, x in enumerate(B):
      d[x].add(i)
    return [d[x].pop() for x in A]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], [3,1,1,4,2]),
  ]
  rslts = [solver.anagramMappings(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
