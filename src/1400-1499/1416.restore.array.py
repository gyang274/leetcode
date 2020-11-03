from functools import lru_cache

class Solution:
  @lru_cache(None)
  def recursive(self, i):
    # init
    if i == self.n:
      return 1
    # main
    count = 0
    for x in range(1, min(self.m, self.n - i) + 1):
      if (int(self.s[i:(i + x)]) <= self.k) and (i + x == self.n or self.s[i + x] != '0'):
        count += self.recursive(i + x)
    return count % (10 ** 9 + 7)
  def numberOfArrays(self, s: str, k: int) -> int:
    self.n, self.s = len(s), s 
    self.m, self.k = len(str(k)), k
    self.recursive.cache_clear()
    return self.recursive(0)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("1000", 10),
    ("1000", 1000),
    ("2020", 30),
    ("1317", 2020),
    ("1234567890", 90),
  ]
  rslts = [solver.numberOfArrays(s, k) for s, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
