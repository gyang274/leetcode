from typing import List


class Solution:
  def sortColors(self, nums: List[int]) -> None:
    """Do not return anything, modify nums in-place instead.
    Two pointers, one pointer from start for 0, another pointer from ende for 2, one pass algorithm.
    """
    n = len(nums)
    # pointer left on 0
    i = 0
    while i < n and nums[i] == 0:
      i += 1
    # pointer right on 2
    k = n - 1
    while k > 0 and nums[k] == 2:
      k -= 1
    # move around 0, 1, 2
    j = i
    while j <= k:
      if nums[j] == 0:
        if j == i:
          j += 1
        else:
          nums[i], nums[j] = nums[j], nums[i]
        i += 1
      elif nums[j] == 2:
        nums[j], nums[k] = nums[k], nums[j]
        k -= 1
      else:
        j += 1
    return None


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [2,0,1],
    [2,0,2,1,1,0], 
  ]
  rslts = [solver.sortColors(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
