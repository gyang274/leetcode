from typing import List
from collections import Counter

class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    x = Counter(arr).values()
    return len(x) == len(set(x))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [1,2,2,3,3,3],
  ]
  rslts = [solver.uniqueOccurrences(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
