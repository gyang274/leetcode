from typing import List

class Solution:
  def recursive(self, i, j):
    if (i, j) not in self.memo:
      if i == j:
        self.memo[(i, j)] = self.nums[i]
      else:
        xi = self.nums[i] + sum(self.nums[(i + 1):(j + 1)]) - self.recursive(i + 1, j)
        xj = self.nums[j] + sum(self.nums[i:j]) - self.recursive(i, j - 1)
        self.memo[(i, j)] = max(xi, xj)
    return self.memo[(i, j)]
  def PredictTheWinner(self, nums: List[int]) -> bool:
    """recursive + memorization
    """
    n = len(nums)
    if n == 0:
      return True
    self.nums = nums
    self.memo = {}
    i, j = 0, n - 1
    x = self.recursive(i, j)
    return x >= sum(nums) / 2.0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [1, 4, 2],
    [1, 4, 23, 7],
  ]
  rslts = [solver.PredictTheWinner(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")