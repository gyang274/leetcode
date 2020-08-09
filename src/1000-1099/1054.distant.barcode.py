from typing import List
from collections import Counter

import heapq

class Solution:
  def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
    n = len(barcodes)
    # heapq
    barCount = [[-v, k] for k, v in Counter(barcodes).items()]
    heapq.heapify(barCount)
    ans = [0] * n
    for i in range(0, n, 2):
      x = heapq.heappop(barCount)
      ans[i] = x[1]
      x[0] += 1
      if i + 1 < n:
        y = heapq.heappop(barCount)
        ans[i + 1] = y[1]
        y[0] += 1
        if y[0] < 0:
          heapq.heappush(barCount, y)
      if x[0] < 0:
        heapq.heappush(barCount, x)
    return ans

class Solution:
  def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
    count = Counter(barcodes)
    barcodes.sort(key=lambda x: (count[x], x))
    barcodes[1::2], barcodes[::2] = barcodes[0:len(barcodes) // 2], barcodes[len(barcodes) // 2:]
    return barcodes

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,1,1,2,2,2],
    [1,1,1,1,2,2,3,3],
    [7,7,7,8,5,7,5,5,5,8],
  ]
  rslts = [solver.rearrangeBarcodes(barcodes) for barcodes in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
