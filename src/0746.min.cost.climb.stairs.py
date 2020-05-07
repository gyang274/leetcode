class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    for i in range(2, len(cost)):
      cost[i] = min(cost[i - 2], cost[i - 1]) + cost[i]
    return min(cost[-2], cost[-1])
