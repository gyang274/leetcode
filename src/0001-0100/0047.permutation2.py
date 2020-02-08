from typing import List


class Solution:
  def permuteUniqueRecursive(self, sets, perm, nums):
    if len(nums) == 0:
      sets.append(perm)
    else:
      numsUnique = set(nums)
      for x in numsUnique:
        numsLeft = nums.copy()
        permCopy = perm.copy()
        numsLeft.remove(x)
        permCopy.append(x)
        self.permuteUniqueRecursive(sets, permCopy, numsLeft)
  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    sets = []
    self.permuteUniqueRecursive(sets, [], nums)
    return sets


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 1, 2],
    [1, 2, 1],
    [1, 2, 2],
    [1, 1, 1],
  ]
  rslts = [solver.permuteUnique(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")