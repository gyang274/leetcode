from typing import List

class Solution:
  def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
    """Q0435, greedy approach.
    """
    s = []
    intervals.sort(key=lambda x: (x[1], -x[0]))
    for interval in intervals:
      if s and s[-2] >= interval[0]:
        continue
      elif s and s[-1] >= interval[0]:
        s.append(interval[1])
      else:
        s.extend([interval[1] - 1, interval[1]])
    return len(s)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,3],[1,4],[2,5],[3,5]],
    [[1,2],[2,3],[2,4],[4,5]],
    [[16,18],[11,18],[15,23],[1,16],[10,16],[6,19],[18,20],[7,19],[10,11],[11,23],[6,7],[23,25],[1,3],[7,12],[1,13],[23,25],[10,22],[23,25],[0,19],[0,13],[7,12],[14,19],[8,17],[7,23],[4,24]],
  ]
  rslts = [solver.intersectionSizeTwo(intervals) for intervals in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
