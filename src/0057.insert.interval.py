from typing import List

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    # intervals, n = sorted(intervals, key=lambda x: x[0]), len(intervals)
    if n == 0:
      return [newInterval]
    connected, i, inserted = [], 0, False
    while i < len(intervals):
      if not inserted:
        if intervals[i][1] < newInterval[0]:
          continue
        elif intervals[i][0] <= newInterval[0] <= intervals[i][1]:
          inserted = True
        elif newInterval[0] < intervals[i]
      
      
      print(connected, interval, r)
      if interval[0] <= r:
        connected[i][1] = r = max(connected[i][1], interval[1])
      else:
        connected.append(interval)
        i += 1
        r = interval[1]
    return connected


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([[1,3],[6,9]], [2,5]),
    ([[1,3],[6,9]], [2,6]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),
  ]
  rslts = [solver.merge(intervals) for intervals in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")