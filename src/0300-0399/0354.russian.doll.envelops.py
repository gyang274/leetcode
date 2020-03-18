from typing import List

class Solution:
  def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    """Q0300: O(NlogN), sort the envelops w.r.t width going up and same width height going down so add a level once can,
      and then find and shrink height to the lowest height for next level like in longest increasing senqueence.
    """
    # view width as index (careful on the equal width case) and height as value for longest increasing senqueence.
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    x = []
    for w, h in envelopes:
      if not x or (x[-1][0] < w and x[-1][1] < h):
        x.append([w, h])
      else:
        l, r = 0, len(x)
        while l < r:
          m = l + (r - l) // 2
          if x[m][1] < h:
            l = m + 1
          else:
            r = m
        x[l][1] = h
    return len(x)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[2,2],[3,3],[4,5],[4,4],[5,5]],
    [[2,2],[3,3],[4,5],[5,5],[4,4]],
    [[2,2],[3,3],[4,5],[5,5],[5,5]],
    [[2,2],[5,12],[12,5],[3,6],[6,3],[7,4]],
    [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]],
  ]
  rslts = [solver.maxEnvelopes(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")