from typing import List

class Solution:
  def lastStoneWeightII(self, stones: List[int]) -> int:
    # modified knapsack, modified coin change Q0518
    # dp has the set of sum of weights of one group
    dp = {0}
    for x in stones:
      dp |= {z + x for z in dp}
    s = sum(stones)
    return min(abs(s - 2 * z) for z in dp)

class Solution:
  def lastStoneWeightII(self, stones: List[int]) -> int:
    # adapt the dp to this problem specifically
    # dp has the set of differences of two groups of stones
    dp = {0}
    for x in stones:
      dp = {x + z for z in dp} | {x - z for z in dp}
    return min(abs(z) for z in dp)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,7,1,4,5,8],
  ]
  rslts = [solver.lastStoneWeightII(stones) for stones in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")