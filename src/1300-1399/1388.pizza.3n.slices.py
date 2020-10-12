from typing import List

class Solution:
  def dp(self, i, j, k, l):
    # max by taking k from s[i:j] assume cycle if l = 1 else no-cycle
    if (i, j, k, l) not in self.memo:
      if k == 1:
        self.memo[(i, j, k, l)] = max(self.s[i:j])
      elif j - i < 2 * k - 1:
        self.memo[(i, j, k, l)] = float('-inf')
      else:
        # max of taking self.s[i] and not taking self.s[i] at this step
        self.memo[(i, j, k, l)] = max(self.dp(i + 2, j - l, k - 1, 0) + self.s[i], self.dp(i + 1, j, k, 0))
    return self.memo[(i, j, k, l)]
  def maxSizeSlices(self, slices: List[int]) -> int:
    # Q0213, dynamic programming
    self.memo, self.s, n = {}, slices, len(slices)
    return self.dp(0, n, n // 3, 1)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [3,1,2],
    [1,2,3,4,5,6],
    [8,9,8,6,1,1],
    [4,1,2,5,8,3,1,9,7],
  ]
  rslts = [solver.maxSizeSlices(slices) for slices in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
