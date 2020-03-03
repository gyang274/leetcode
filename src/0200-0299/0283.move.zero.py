from typing import List

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    """Do not return anything, modify nums in-place instead.
      Two pointers, i: 1st zero, j: 1st none-zero, if i > -1 and j < n switch, i += 1, j += 1.
    """
    i, n = -1, len(nums)
    for j in range(n):
      if nums[j] == 0:
        if i == -1:
          i = j
      else:
        if i > -1:
          nums[i], nums[j] = nums[j], nums[i]
          i += 1
    return None

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    """Do not return anything, modify nums in-place instead.
      Two pointers, i: last none zero, j: moving index, make sure elements after i are all 0.
    """
    i, n = 0, len(nums)
    for j in range(n):
      if not nums[j] == 0:
        # if i < j:
        #   nums[i], nums[j] = nums[j], nums[i]
        # it is ok to switch with itself when i == j, eliminate the cost in if condition
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
    return None

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [0],
    [1],
    [0,0],
    [0,1],
    [1,0],
    [0,1,0,2,3,0],
  ]
  rslts = [solver.moveZeroes(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")