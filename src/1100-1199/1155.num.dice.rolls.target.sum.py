from functools import lru_cache

class Solution:
  @lru_cache(None)
  def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    M = 10 ** 9 + 7
    if target < d or target > d * f:
      return 0
    if d == 1:
      return 1
    return sum(self.numRollsToTarget(d - 1, f, target - x) for x in range(1, min(target, f + 1))) % M

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (20, 30, 500),
  ]
  rslts = [solver.numRollsToTarget(d, f, target) for d, f, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
