from typing import List


class Solution:
  def insertLocation(self, intervals: List[List[int]], x: int) -> int:
    l, r = 0, 2 * len(intervals)
    i = (l + r) // 2
    while l < r:
      # print(f'init: {x=}, {l=}, {r=}, {i=}')
      if i % 2 == 0:
        if intervals[(i - 1) // 2][(i - 1) % 2] < x < intervals[i // 2][i % 2]:
          break
        elif x <= intervals[(i - 1) // 2][(i - 1) % 2]:
          r = i
        else:
          l = i
      else:
        if intervals[(i - 1) // 2][(i - 1) % 2] <= x <= intervals[i // 2][i % 2]:
          break
        elif x < intervals[(i - 1) // 2][(i - 1) % 2]:
          r = i - 1
        else:
          l = i + 1
      i = (l + r) // 2
      # print(f'next: {x=}, {l=}, {r=}, {i=}')
    return i
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """Key: invertals are non-overlapping, so [interval[i][0], interval[i][1], ..] are sorted, it is straightforward to
      look for index j, k for newInterval[0], newInterveral[1] in the list and connect.
      Time: O(2log(2n)), n = len(intervals) for search j, k, and O(k - j) for connect - worset case O(n).
    """
    # add float("-inf") on the left and float("inf") on the right
    """
      interval:       -inf, [0, 2], [3, 5], [8, 13], +inf
      interval index:         0       1       2
      flex-out index:     0   1   2   3   4   5    6
    """
    if not intervals:
      return [newInterval]
    # print(f'{intervals=}, {newInterval=}')
    j = self.insertLocation(intervals, newInterval[0])
    # print(f"{j=}")
    k = self.insertLocation(intervals, newInterval[1])
    # print(f"{k=}")
    return intervals[:(j // 2)] + [[
      min(newInterval[0], intervals[j // 2][0]) if j < 2 * len(intervals) else newInterval[0], 
      max(intervals[(k - 1) // 2][1] , newInterval[1]) if k > 0 else newInterval[1]
    ]] + intervals[((k + 1) // 2):]


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([], [5,7]),
    ([[2,5]], [0,1]),
    ([[2,5]], [1,2]),
    ([[2,5]], [1,3]),
    ([[2,5]], [2,3]),
    ([[2,5]], [3,4]),
    ([[2,5]], [4,5]),
    ([[2,5]], [4,6]),
    ([[2,5]], [5,6]),
    ([[2,5]], [6,7]),
    ([[1,3],[6,9]], [2,5]),
    ([[1,3],[6,9]], [2,6]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),
  ]
  rslts = [solver.insert(intervals, newInterval) for intervals, newInterval in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")