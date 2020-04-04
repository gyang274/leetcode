from typing import List

class Solution:
  def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    """O(MN), max of min dist.
    """
    dist = 0
    for h in houses:
      dist = max(dist, min([abs(h - t) for t in heaters]))
    return dist

class Solution:
  def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    """O(max(M, N)log(max(M, N)))
    """
    houses.sort(); heaters.sort()
    d, i, j, m, n = 0, 0, 0, len(houses), len(heaters)
    while i < m:
      while j < n - 1 and abs(houses[i] - heaters[j + 1]) <= abs(houses[i] - heaters[j]):
        j += 1
      d = max(d, abs(houses[i] - heaters[j]))
      i += 1
    return d

class Solution:
  def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    """O(max(M, N)log(max(M, N)))
    """
    houses.sort(); heaters.sort()
    d, j, n = 0, 0, len(heaters)
    for h in houses:
      while j < n - 1 and abs(h - heaters[j + 1]) <= abs(h - heaters[j]):
        j += 1
      d = max(d, abs(h - heaters[j]))
    return d

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([], []),
    ([1], [1]),
    ([1,2,3], [2]),
    ([1,2,3,4], [1,4]),
    ([1,1,1,1,1,1,999,999,999,999,999], [499,500,501]),
  ]
  rslts = [solver.findRadius(houses, heaters) for houses, heaters in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")   