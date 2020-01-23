from typing import List


class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    """Binary search target value with `<=` replacing `==`.
    """
    # corner case
    if len(nums) == 0: return 0
    # main
    m, l, r = 0, 0, len(nums) - 1
    while l <= r:
      m = (l + r) // 2
      if target <= nums[m]:
        r = m - 1
      else:
        l = m + 1
    if target <= nums[m]:
      return m
    else:
      return m + 1

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([], 0),
    ([2, 3, 5, 8], 1),
    ([2, 3, 5, 8], 2),
    ([2, 3, 5, 8], 3),
    ([2, 3, 5, 8], 4),
    ([2, 3, 5, 8], 5),
    ([2, 3, 5, 8], 6),
    ([2, 3, 5, 8], 7),
    ([2, 3, 5, 8], 8),
    ([2, 3, 5, 8], 9),
  ]
  rslts = [solver.searchInsert(nums, target) for nums, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")