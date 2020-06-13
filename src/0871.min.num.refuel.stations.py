from typing import List

import heapq

class Solution:
  def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
    """TC: O(NlogN), SC: O(N).
    """
    # maintain a priority queue of gas for stations passed by, fuel when out of gas only,
    # imagine that we can travel and remember the stations, gas, and tel-fuel when needed
    tank, seen, stop = startFuel, [], 0
    stations.sort(reverse=True)
    while tank < target and (stations or seen):
      while stations and tank >= stations[-1][0]:
        heapq.heappush(seen, -stations.pop()[1])
      if seen:
        tank -= heapq.heappop(seen)
        stop += 1
      else:
        return -1
    return -1 if tank < target else stop

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 1, []),
    (3, 2, []),
    (100, 50, [[40,50]]),
    (100, 10, [[10,60],[20,30],[30,30],[60,40]]),
    (1000, 299, [[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]),
    (1000000, 70768, [[12575,171159],[81909,101253],[163732,164401],[190025,65493],[442889,31147],[481202,166081],[586028,206379],[591952,52748],[595013,9163],[611883,217156]]),
  ]
  rslts = [solver.minRefuelStops(target, startFuel, stations) for target, startFuel, stations in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
