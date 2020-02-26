from typing import List
from itertools import chain

class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    """status machine: min num meeting room is the max num of meeting on the same time, O(NlogN).
      Key: keep a counter, sort intervals by each meeting start and end time along with meeting index, 
        for any one start +1, and end of previous one -1.
    """
    counter, xmin = 0, 0
    # meeting's start and ende time with index, 
    # sort by time, ende -1/start +1 (ende first than start, in case ende one and start next at the same time)
    mtse = list(chain.from_iterable(((s, 1), (e, -1)) for s, e in intervals))
    mtse.sort()
    for mt, se in mtse:
      if se == 1:
        counter += 1
      else:
        counter -= 1
      xmin = max(xmin, counter)
    return xmin

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([]),
    ([[2,3]]),
    ([[2,3],[3,5]]),
    ([[2,4],[3,5]]),
    ([[7,10],[2,4]]),
    ([[0,30],[5,10],[15,20]]),
    ([[0,30],[5,10],[15,20]]),
  ]
  rslts = [solver.minMeetingRooms(intervals) for intervals in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")