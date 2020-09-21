from typing import List
from collections import defaultdict

class Solution:
  def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
    d = defaultdict(list)
    for i, x in enumerate(groupSizes):
      d[x].append(i)
    ans = []
    for x in d:
      for k in range(0, len(d[x]), x):
        ans.append(d[x][k:(k + x)])
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,2,3,3],
    [2,1,3,2,3,3],
    [2,1,3,2,1,3,3],
    [2,1,3,2,2,3,2,3],
  ]
  rslts = [solver.groupThePeople(groupSizes) for groupSizes in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
