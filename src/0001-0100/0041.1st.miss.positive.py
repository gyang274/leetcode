from typing import List


class Solution:
  def firstMissingPositive(self, nums: List[int]) -> int:
    """Key: in-place switch nums, so nums[i] == i + 1, i += 1, return i += 1.
    """
    i = 0
    k = len(nums) - 1
    while i <= k:
      v = nums[i]
      if v == i + 1:
        i += 1
      elif v <= 0 or v > k + 1 or nums[v - 1] == v:
        nums[i] = nums[k]
        k -= 1 
      else:
        nums[i], nums[v - 1] = nums[v - 1], nums[i]
    return i + 1


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [],
    [0],
    [1],
    [2],
    [0, 1, 2],
    [1, 2, 3],
    [3, 4, 0, 2],
    [3, 4, -1, 1],
    [7, 8, 9, 11, 12],
  ]
  rslts = [solver.firstMissingPositive(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")