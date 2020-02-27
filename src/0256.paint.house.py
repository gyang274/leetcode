from typing import List

class Solution:
  def minCost(self, cost: List[List[int]]) -> int:
    """Solutions:
      1. Graph + Dijkstra's Algorigthm for Shortest Path.
        1) create sentinel `init` and `ende` node with cost 0, create a node nij for each house i color j with cost cij.
        2) connect `init` to all house 0 nodes, connect house i nodes to house i + 1 nodes with different colors, and
          connect all last house nodes to `ende`.
        3) convert node cost to edge cost by setting the edge cost as the average of the nodes cost its connected, e.g.
          cost(edeg<nodeX, nodeY>) = cost(nodeX, nodeY)
        4) now the question is equivalent to find the shortest path (path with min cost) from `init` to `ende`
        5) due to the structure of the problem set up, the algorithm will run in O(V) instead of O(E + VlogV).
      2. Dynamic programming, maintain series of cost for (house i, color j), update house i + 1 accordingly.
        dp[i][j] = min(dp[i-1][:j] + dp[i-1][(j+1):]) + c[i][j]
        This is memoryless, so status machine.
    """
    n = len(cost)
    if n == 0:
      return 0
    m = len(cost[0])
    if m == 0:
      return 0
    if m == 1:
      if n == 1:
        return min(cost[0])
      else:
        # raise?
        return -1
    s = [0] * m
    for i in range(n):
      t = [0] * m
      for j in range(m):
        # min cost upto i'th house with j'th color
        # min of (i-1)'th house with a differnt color and i'th house j'th color cost
        t[j] = min(s[:j] + s[(j + 1):]) + cost[i][j]
      s = t
    return min(s)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [[]],
    [[1]],
    [[1], [2]],
    [[17,2,17],[16,16,5],[14,3,19]],
  ]
  rslts = [solver.minCost(cost) for cost in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")