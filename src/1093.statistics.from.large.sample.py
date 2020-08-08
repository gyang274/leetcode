from typing import List

class Solution:
  def sampleStats(self, count: List[int]) -> List[float]:
    # counts
    csum = sum(count)
    # index of median, mode
    cmedianL, cmedianH, xmedianL, xmedianH, cmode, xmode = (csum - ((csum & 1) ^ 1)) // 2, csum // 2, -1, -1, 0, -1
    # O(N)
    cc, xsum, xmin, xmax = 0, 0, -1, -1
    for x, c in enumerate(count):
      cc += c
      if xmin < 0 and c > 0:
        xmin = x
      if xmedianL < 0 and cc > cmedianL:
        xmedianL = x
      if xmedianH < 0 and cc > cmedianH:
        xmedianH = x
      if c > cmode:
        cmode, xmode = c, x
      if c > 0:
        xmax = max(xmax, x)
      xsum += x * c
    return [xmin, xmax, xsum / csum, (xmedianL + xmedianH) / 2.0, xmode]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    ],
  ]
  rslts = [solver.sampleStats(count) for count in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
