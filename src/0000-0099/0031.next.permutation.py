from typing import List

class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    """Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    i = n - 1
    while i > 0 and nums[i] <= nums[i - 1]:
      i -= 1
    if i == 0:
      for k in range(n // 2):
        nums[k], nums[n - 1 - k] = nums[n - 1 - k], nums[k]
    else:
      j = i
      while j < n and nums[j] > nums[i - 1]:
        j += 1
      nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
      for k in range((n - i) // 2):
        nums[i + k], nums[n - 1 - k] = nums[n - 1 - k], nums[i + k]
    # return None

if __name__ == '__main__':
  solver = Solution()
  cases = [
    # [],
    [1],
    [1, 2, 3],
    [1, 3, 2],
    [3, 2, 1],
    [1, 1, 4],
    [1, 4, 1],
    [4, 1, 1],
    [1, 3, 4, 2],
    [1, 4, 3, 2],
  ]
  rslts = [solver.nextPermutation(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")