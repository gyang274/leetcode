from typing import List
from collections import Counter

class Solution:
  def minSetSize(self, arr: List[int]) -> int:
    xs, n = sorted(Counter(arr).values(), reverse=True), len(arr)
    count = 0
    for i, x in enumerate(xs):
      count += x
      if count >= n // 2:
        return i + 1
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.minSetSize(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
