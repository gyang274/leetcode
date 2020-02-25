from typing import List

class Solution:
  def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    # if len(intervals) < 2:
    #   return True
    # sort the interval w.r.t start time
    intervals.sort()
    for i in range(1, len(intervals)):
      if intervals[i][0] < intervals[i - 1][1]:
        return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([]),
    ([[2,3]]),
    ([[2,3],[3,5]]),
    ([[7,10],[2,4]]),
    ([[0,30],[5,10],[15,20]]),
  ]
  rslts = [solver.canAttendMeetings(intervals) for intervals in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")