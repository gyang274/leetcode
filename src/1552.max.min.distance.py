from typing import List

class Solution:
  def maxDistance(self, position: List[int], m: int) -> int:
    # binary search O(NlogQ), n = len(position), q = max(position)
    position.sort()
    def maxBalls(d):
      # O(N), if distance >= d, how many magnetic balls can be placed?
      count, p = 0, -d
      for x in position:
        if x - p >= d:
          count, p = count + 1, x
      return count
    l, r = 0, max(position)
    while l < r:
      d = r - (r - l) // 2
      if maxBalls(d) >= m:
        l = d
      else:
        r = d - 1
    return l

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,4,7], 3),
    ([5,4,3,2,1,1000000000], 2),
  ]
  rslts = [solver.maxDistance(position, m) for position, m in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
