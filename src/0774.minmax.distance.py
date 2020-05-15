from typing import List

import heapq, math

class Solution:
  def minmaxGasDist(self, stations: List[int], K: int) -> float:
    q = [(-(stations[i] - stations[i - 1]), 1) for i in range(1, len(stations))]
    heapq.heapify(q)
    for _ in range(K):
      d, k = heapq.heappop(q)
      heapq.heappush(q, (d * k / (k + 1), k + 1))
    return -q[0][0]

class Solution:
  def minmaxGasDist(self, stations: List[int], K: int) -> float:
    q = [(-(stations[i] - stations[i - 1]), 1) for i in range(1, len(stations))]
    heapq.heapify(q)
    while K > 0:
      d, k = heapq.heappop(q)
      # i = 1
      # while i < K and d * k / (k + i) < q[0][0]:
      #   i += 1
      i = min(max(1, math.ceil(d * k / q[0][0] - k)), K)
      print(i)
      heapq.heappush(q, (d * k / (k + i), k + i))
      K -= i
    return -q[0][0]

class Solution:
  def minmaxGasDist(self, stations: List[int], K: int) -> float:
    def achievable(d):
      return sum(int((stations[i + 1] - stations[i]) / d) for i in range(len(stations) - 1)) <= K
    l, r = 0, 1e8
    while r - l >= 1e-6:
      m = (l + r) / 2.0
      if achievable(m):
        r = m
      else:
        l = m
    return l

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,4,5,6,7,8,9,10], 9),
  ]
  rslts = [solver.minmaxGasDist(stations, K) for stations, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
