from typing import List

class Solution:
  def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
    d = {}
    for region in regions:
      for child in region[1:]:
        d[child] = region[0]
    p1 = [region1]
    for r1 in p1:
      if r1 in d:
        p1.append(d[r1])
    p2 = [region2]
    for r2 in p2:
      if r2 in d:
        p2.append(d[r2])
    s2 = set(p2)
    for r1 in p1:
      if r1 in s2:
        return r1
    return ""

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]], "Quebec", "New York"),
  ]
  rslts = [solver.findSmallestRegion(regions, region1, region2) for regions, region1, region2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
