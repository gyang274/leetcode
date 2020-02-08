from typing import List


class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    """
    Keep 2 pointers, 1 explore and 1 record the position to switch.
    """
    i = 0
    j = 0
    x = None
    while i < len(nums):
      if not nums[i] == x:
        x = nums[i]
        if j < i:
          nums[j], nums[i] = nums[i], nums[j]
        j += 1
      i += 1
    return j


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [],
    [1],
    [1,2],
    [1,1,2],
    [0,0,1,1,1,2,2,3,3,4],
  ]
  rslts = [solver.removeDuplicates(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")