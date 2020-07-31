from typing import List

import heapq

class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    stones = list(map(lambda x: -x, stones))
    heapq.heapify(stones)
    while len(stones) > 1:
      y, x = heapq.heappop(stones), heapq.heappop(stones)
      if y < x:
        heapq.heappush(stones, y - x)
    return -stones[0] if stones else 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,7,1,4,5,8],
  ]
  rslts = [solver.lastStoneWeight(stones) for stones in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
