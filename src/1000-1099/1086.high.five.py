from typing import List
from collections import defaultdict

import heapq

class Solution:
  def highFive(self, items: List[List[int]]) -> List[List[int]]:
    # s: id -> score
    s = defaultdict(list)
    for i, x in items:
      s[i].append(-x)
    # z: (id, high-five)
    z = []
    for i in s:
      heapq.heapify(s[i])
      m = 0
      for _ in range(5):
        m -= heapq.heappop(s[i])
      z.append((i, m // 5))
    return sorted(z)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]],
  ]
  rslts = [solver.highFive(items) for items in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
