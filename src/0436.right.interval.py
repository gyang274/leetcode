from typing import List

class Solution:
  def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
    """sort by start and ende + two pointers, O(NlogN).
    """
    n = len(intervals)
    # intervals with index
    ii = [(s, e, i) for i, (s, e) in enumerate(intervals)]
    # sort w.r.t start
    ss = sorted(ii, key=lambda x: (x[0], x[1]))
    # sort w.r.t endes
    se = sorted(ii, key=lambda x: (x[1], x[0]))
    # one pass
    i, j, ans = 0, 0, [-1] * n
    while i < n and j < n:
      if se[i][1] <= ss[j][0]:
        # found the right intervals with smallest start point
        ans[se[i][2]] = ss[j][2]
        i += 1
      else:
        j += 1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [[0,1]],
    [[3,4],[2,3],[1,2]],
    [[1,4],[2,3],[3,4]],
  ]
  rslts = [solver.findRightInterval(intervals) for intervals in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
        