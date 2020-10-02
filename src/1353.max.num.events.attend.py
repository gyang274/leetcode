from typing import List
from collections import deque

import heapq

class Solution:
  def maxEvents(self, events: List[List[int]]) -> int:
    # alast: the time attend last event
    count, alast = 0, 0
    heapq.heapify(events)
    while events:
      s, e = heapq.heappop(events)
      if s <= alast:
        if e > alast:
          if e == alast + 1:
            alast += 1
            count += 1
          else:
            heapq.heappush(events, [alast + 1, e])
      else:
        alast = max(alast + 1, s)
        count += 1
    return count

class Solution:
  def maxEvents(self, events: List[List[int]]) -> int:
    # alast: the time attend last event
    count, alast = 0, 0
    # eholds: events hold for attending
    events, eholds = deque(sorted(events)), []
    while events or eholds:
      # move the days
      if not eholds:
        alast = events[0][0]
      # next events available for attending
      while events and events[0][0] <= alast:
        heapq.heappush(eholds, events.popleft()[1])
      # attend the one soonest expired
      heapq.heappop(eholds)
      # move the days as spent attend event
      alast += 1
      count += 1
      # remove events expired
      while eholds and eholds[0] < alast:
        heapq.heappop(eholds)
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,1]],
    [[1,2],[2,3],[3,4]],
    [[1,2],[1,2],[2,3],[3,4]],
    [[1,1],[1,4],[2,2],[3,4],[4,4]],
    [[1,5],[1,5],[1,5],[2,3],[2,3]],
    [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]],
  ]
  rslts = [solver.maxEvents(events) for events in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
