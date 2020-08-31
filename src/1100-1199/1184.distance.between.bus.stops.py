from typing import List
from itertools import accumulate

class Solution:
  def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
    # prefix sum of distance
    # distance(i, j) = prefix[j] - prefix[i]
    prefix, s = list(accumulate(distance, initial=0)), sum(distance)
    x = abs(prefix[destination] - prefix[start])
    return min(x, s - x) 

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,4], 0, 1),
    ([1,2,3,4], 0, 2),
    ([1,2,3,4], 0, 3),
    ([1,2,3,4], 2, 0),
    ([1,2,3,4], 2, 1),
    ([1,2,3,4], 2, 3),
  ]
  rslts = [solver.distanceBetweenBusStops(distance, start, destination) for distance, start, destination in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
