from typing import List
from collections import defaultdict

class Solution:
  def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
    # O(NlogN) sort
    d, x = defaultdict(lambda: 0), sorted(list(zip(values, labels)), reverse=True)
    # O(N) one pass
    ans, num = 0, 0
    for v, l in x:
      if num < num_wanted:
        if d[l] < use_limit:
          num += 1
          ans += v
          d[l] += 1
      else:
        break
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([5,4,3,2,1], [1,1,2,2,3], 3, 1),
    ([5,4,3,2,1], [1,3,3,3,2], 3, 2),
    ([9,8,8,7,6], [0,0,0,1,1], 3, 1),
    ([9,8,8,7,6], [0,0,0,1,1], 3, 2),
  ]
  rslts = [solver.largestValsFromLabels(values, labels, num_wanted, use_limit) for values, labels, num_wanted, use_limit in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
