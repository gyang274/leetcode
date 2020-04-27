from typing import List

import itertools

class Solution:
  def judgePoint24(self, nums: List[int]) -> bool:
    """O(1), brute force, limited combinations of 9216.
    """
    n = len(nums)
    if n == 0:
      return False
    if n == 1:
      return abs(nums[0] - 24) < 1e-7
    for p in itertools.permutations(nums):
      p = list(p)
      x, y = p.pop(), p.pop()
      zs = [x + y, x - y, x * y]
      if abs(y) > 1e-7:
        zs.append(x / y)
      for z in zs:
        if self.judgePoint24(p + [z]):
          return True
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,1,1,1],
    [4,1,8,7],
  ]
  rslts = [solver.judgePoint24(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
