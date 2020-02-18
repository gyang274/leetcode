from typing import List

class Solution:
  def combinationSum3Recursive(self, prefix, xset, k, n):
    if k == 1:
      if n in xset:
        self.ans.append(prefix + [n])
    elif k > 1:
      for i, x in enumerate(xset):
        xmin = (k - 1) * k / 2
        if xmin <= n - x <= 10 * (k - 1) - xmin:
          self.combinationSum3Recursive(prefix + [x], xset[(i + 1):], k - 1, n - x)
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    self.ans = []
    self.combinationSum3Recursive([], [x for x in range(1, 10)], k, n)
    return self.ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 4),
    (3, 7),
    (3, 9),
  ]
  rslts = [solver.combinationSum3(k, n) for k, n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")