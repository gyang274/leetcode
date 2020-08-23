from typing import List

import heapq

class Solution:
  def connectSticks(self, sticks: List[int]) -> int:
    # Huffman's algorithm, TC: O(NlogN), SC: O(N).
    cost = 0
    heapq.heapify(sticks)
    while len(sticks) > 1:
      x, y = heapq.heappop(sticks), heapq.heappop(sticks)
      cost += x + y
      heapq.heappush(sticks, x + y)
    return cost

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [2,3,5,8,6],
  ]
  rslts = [solver.connectSticks(sticks) for sticks in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
