from typing import List

class Solution:
  def _(self, i):
    return -1
  def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
    # TC: o(N), SC: O(N), sliding window
    n = len(boxes)
    # greedy taking as much as possible, only when the current one needs a new ship and it has the same destinate port
    # with the last severals from previous ship, then move those to the same ship..
    X, mb, mw = boxes, maxBoxes, maxWeight
    # dp: num of trips
    dp = [0] * (n + 1)
    # k: cursor index, load all boxes from cursor index to i-th index in one voyage
    # sw, sp: current weight on the ship, and count of consecutive ports between cursor and i-th index
    k, sw, sp = 0, 0, 0
    # sliding index k..
    for i in range(n):
      if i - k == mb:
        # move cursor because of max boxes constraint
        sw -= X[k][1]
        if X[k][0] != X[k + 1][0]:
          sp -= 1
        k += 1
      # add ith box, update ship weight and ports
      sw += X[i][1]
      if i > 0 and X[i][0] != X[i - 1][0]:
        sp += 1
      # move cursor because of max weights constraint
      while sw > mw:
        sw -= X[k][1]
        if X[k][0] != X[k + 1][0]:
          sp -= 1
        k += 1
      # move cursor if no benefit to carry items on last ship (move to previous one)
      while k < i and dp[k] == dp[k + 1]:
        sw -= X[k][1]
        if X[k][0] != X[k + 1][0]:
          sp -= 1
        k += 1
      # dp: set num of trips
      dp[i + 1] = dp[k] + sp + 2
    return dp[n]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[1,1],[2,1]], 2, 3, 2),
    ([[1,1],[2,1],[2,1]], 2, 3, 2),
    ([[1,1],[2,1],[2,1],[2,1]], 2, 3, 2),
    ([[1,1],[2,1],[2,1],[2,1],[2,1]], 2, 3, 2),
  ]
  rslts = [solver.boxDelivering(boxes, portsCount, maxBoxes, maxWeight) for boxes, portsCount, maxBoxes, maxWeight in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
