from typing import List

class Solution:
  def dfs(self, i, t):
    tt = tuple(t)
    if (i, tt) not in self.memo:
      if sum(t) == 0:
        self.memo[(i, tt)] = True
      else:
        for k in range(4):
          if t[k] - self.nums[i] >= 0:
            t[k] -= self.nums[i]
            r = self.dfs(i + 1, t)
            t[k] += self.nums[i]
            if r:
              self.memo[(i, tt)] = True
              break
        if (i, tt) not in self.memo:
          self.memo[(i, tt)] = False
    return self.memo[(i, tt)]
  def makesquare(self, nums: List[int]) -> bool:
    """dfs/backtrack + memorization
    """
    n, s = len(nums), sum(nums)
    if not (n >= 4 and s > 0 and s % 4 == 0 and max(nums) <= s // 4):
      return False
    self.nums, self.memo = nums, {}
    self.nums.sort(reverse=True)
    return self.dfs(0, [s // 4] * 4)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,1,2,2,2],
    [3,3,3,3,4],
    [1,1,2,8,9,9,10],
  ]
  rslts = [solver.makesquare(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")