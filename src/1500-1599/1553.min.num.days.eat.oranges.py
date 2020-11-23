from functools import lru_cache

class Solution:
  @lru_cache(None)
  def minDays(self, n: int) -> int:
    if n < 2:
      return n
    return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.minDays(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
