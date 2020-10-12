from functools import lru_cache

class Solution:
  @lru_cache(None)
  def recursive(self, i, j):
    if i >= j:
      return 0
    if self.s[i] == self.s[j]:
      return self.recursive(i + 1, j - 1)
    else:
      return min(self.recursive(i + 1, j), self.recursive(i, j - 1)) + 1
  def minInsertions(self, s: str) -> int:
    self.s = s
    self.recursive.cache_clear()
    return self.recursive(0, len(s) - 1)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "zzazz",
    "mbadm",
    "leetcode"
  ]
  rslts = [solver.minInsertions(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
