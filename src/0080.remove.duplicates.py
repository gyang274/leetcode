from typing import List


class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
      return n
    i, j, v0, v1 = 2, 2, nums[0], nums[1]
    while j < n:
      # print(f'init: {i=}, {j=}, {v0=}, {v1=}')
      if not v0 == v1 == nums[j]:
        v0, v1 = v1, nums[j]
        if i < j:
          # nums[i], nums[j] = nums[j], nums[i]
          nums[i] = nums[j]
        i += 1
      j += 1
      # print(f'ende: {i=}, {j=}, {v0=}, {v1=}')
    return i


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [],
    [0],
    [0,0,0,0],
    [1,1,1,2,2,3],
    [0,0,1,1,1,1,2,3,3],
  ]
  rslts = [solver.removeDuplicates(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")