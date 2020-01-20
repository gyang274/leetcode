from typing import List


class Solution:
  def permuteRecursive(self, sets, perm, nums):
    if len(nums) == 0:
      sets.append(perm)
    else:
      for i in range(len(nums)):
        numsLeft = nums.copy()
        permCopy = perm.copy()
        permCopy.append(numsLeft.pop(i))
        self.permuteRecursive(sets, permCopy, numsLeft)
  def permute(self, nums: List[int]) -> List[List[int]]:
    sets = []
    self.permuteRecursive(sets, [], nums)
    return sets


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
  ]
  rslts = [solver.permute(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")