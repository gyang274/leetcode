from typing import List

class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    """sort w.r.t start point + dynamic programming: O(N^2)
    """
    # sort w.r.t start
    intervals.sort()
    # n: num of intervals
    n = len(intervals)
    # dp: max num of intervals can be kept w.o. overlapping up i-th interval
    dp = [1] * n
    for i in range(1, n):
      for j in range(i):
        # i and j are not overlapped
        if intervals[j][1] <= intervals[i][0]:
          dp[i] = max(dp[i], dp[j] + 1)
    return 0 if n == 0 else (n - max(dp))

class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    """sort w.r.t start point + greedy approach: O(NlogN)
    """
    # sort w.r.t start
    intervals.sort()
    # n: num of intervals
    n = len(intervals)
    # keep track the ende points of upto i-th intervals, prefer the one with smaller ende point
    counter, xmax = 0, float("-inf")
    for i in range(n):
      # not overlapped with previous ones
      if xmax <= intervals[i][0]:
        xmax = intervals[i][1]
      else:
        # prefer the one with smaller ende point
        xmax = min(intervals[i][1], xmax)
        counter += 1
    return counter

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [[0,1]],
    [[0,1],[1,2]],
    [[0,1],[0,1],[0,1]],
    [[0,1],[0,2],[1,2],[1,3],[2,3],[3,4]],
  ]
  rslts = [solver.eraseOverlapIntervals(intervals) for intervals in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")