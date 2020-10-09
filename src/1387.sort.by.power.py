from functools import lru_cache

class Solution:
  @lru_cache(None)
  def _power(self, x):
    if x == 1:
      return 0
    if x & 1:
      return self._power(x * 3 + 1) + 1
    else:
      return self._power(x // 2) + 1
  def getKth(self, lo: int, hi: int, k: int) -> int:
    return sorted([(self._power(x), x) for x in range(lo, hi + 1)])[k - 1][1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (7, 11, 4),
    (1, 1000, 777),
  ]
  rslts = [solver.getKth(lo, hi, k) for lo, hi, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
