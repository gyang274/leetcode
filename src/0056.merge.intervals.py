from typing import List


class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals, n = sorted(intervals, key=lambda x: x[0]), len(intervals)
    if n == 0:
      return []
    connected, i, r = [intervals[0]], 0, intervals[0][1]
    for interval in intervals[1:]:
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
    # [[1,3],[2,6],[8,10],[15,18]],
    [[1,4],[0,2],[3,5]],
    # [[1,4],[4,5]],
  ]
  rslts = [solver.merge(intervals) for intervals in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")