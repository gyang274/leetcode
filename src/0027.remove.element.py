from typing import List


class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    """Two pointers.
    """
    i = 0
    n = len(nums)
    while i < n:
      if nums[i] == val:
        nums[i] = nums[n - 1]
        n -= 1
      else:
        i += 1
    return n


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([], 0),
    ([1], 1),
    ([1, 1], 1),
    ([1, 1, 1], 1),
    ([1, 2], 1),
    ([1, 2], 2),
    ([1, 2, 1, 1], 1),
    ([1, 2, 1, 1], 2),
    ([1, 2, 3, 4], 4),
  ]
  rslts = [solver.removeElement(nums, val) for nums, val in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")