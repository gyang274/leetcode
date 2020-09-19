from typing import List

class Solution:
  def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    # sort the interval by (s, e)
    intervals.sort(key=lambda r: (r[0], -r[1]))
    # keep track the interval's ende
    x, k = -1, 0
    for s, e in intervals:
      k += (e <= x)
      x = max(x, e)
    return len(intervals) - k

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2],[1,4],[3,4]],
    [[1,4],[3,6],[2,8]],
  ]
  rslts = [solver.removeCoveredIntervals(intervals) for intervals in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
