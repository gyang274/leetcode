from typing import List

class Solution:
  def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
    remove_start, remove_end = toBeRemoved
    # O(N), one pass, sweep lines
    output = []
    for start, end in intervals: 
      # if current interval ends before toBeRemoved or starts after
      if end <= remove_start or start >= remove_end:
        output.append([start, end])
      # if the interval to be removed is inside of the current interval
      elif start < remove_start and end > remove_end:
        output.append([start, remove_start])
        output.append([remove_end, end])
      # "left" overlap
      elif start < remove_start and end <= remove_end:
        output.append([start, remove_start])
      # "right" overlap
      elif start >= remove_start and end > remove_end:
        output.append([remove_end, end])
    return output

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[0,5]], [2,3]),
    ([[0,2],[3,4],[5,7]], [1,6]),
  ]
  rslts = [solver.removeInterval(intervals, toBeRemoved) for intervals, toBeRemoved in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
