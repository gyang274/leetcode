from typing import List

import heapq

class Solution:
  def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    trips = sorted([(s, t, n) for n, s, t in trips])
    # car: priority queue of (drop-off-location, number of passengers)
    car, num = [], 0
    for s, t, n in trips:
      # lazy drop-off
      while car and car[0][0] <= s:
        num -= heapq.heappop(car)[1]
      # pick-up if possible
      if num + n > capacity:
        return False
      num += n
      heapq.heappush(car, (t, n))
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[2,1,5],[3,3,7]], 4),
    ([[2,1,5],[3,3,7]], 5),
    ([[2,1,5],[3,5,7]], 3),
    ([[3,2,7],[3,7,9],[8,3,9]], 11),
  ]
  rslts = [solver.carPooling(trips, capacity) for trips, capacity in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")