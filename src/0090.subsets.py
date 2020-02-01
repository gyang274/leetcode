from typing import List


class Solution:
  def backtrack(self, sets, x, nums):
    # print(f'{sets=}, {x=}, {nums=}')
    sets.append(x)
    for i in range(len(nums)):
      if i == 0 or nums[i] > nums[i - 1]:
        self.backtrack(sets, x + [nums[i]], nums[(i + 1):])
  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    """Backtracking. Similar as 0047 PermutationUnique.
    """
    sets = []
    nums.sort()
    self.backtrack(sets, [], nums)
    return sets


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [],
    [0],
    [0, 1],
    [0, 1, 1],
    [0, 1, 1, 2, 2, 2], 
  ]
  rslts = [solver.subsetsWithDup(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")