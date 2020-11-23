from typing import List

class Solution:
  def recursive(self, i, k):
    if i == self.n:
      self.m = max(self.m, k)
    else:
      for j in range(i + 1, self.n + 1):
        if k + 1 + (self.n - j) > self.m and self.s[i:j] not in self.x:
          self.x.add(self.s[i:j])
          self.recursive(j, k + 1)
          self.x.remove(self.s[i:j])
  def maxUniqueSplit(self, s: str) -> int:
    # dfs + backtrack
    self.s = s
    self.n = len(s)
    self.m = 1
    self.x = set([])
    self.recursive(0, 0)
    return self.m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "leetcode",
  ]
  rslts = [solver.maxUniqueSplit(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
