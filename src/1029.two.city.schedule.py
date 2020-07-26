from typing import List

class Solution:
  def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    # let the one cost more different choose side first.
    ca, cb, cc, n = 0, 0, 0, len(costs) // 2
    for d, a, b in sorted((-abs(a - b), a, b) for a, b in costs):
      if (a < b and ca < n) or (cb == n):
        ca += 1
        cc += a
      else:
        cb += 1
        cc += b
    return cc

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[10,20],[30,200],[400,50],[30,20]],
  ]
  rslts = [solver.twoCitySchedCost(costs) for costs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
