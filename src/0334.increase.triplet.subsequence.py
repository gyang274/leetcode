from typing import List

class Solution:
  def increasingTriplet(self, nums: List[int]) -> bool:
    xmin = [2147483647, 2147483647]
    for i in range(len(nums)):
      if nums[i] > xmin[1]:
        return True
      elif nums[i] > xmin[0]:
        xmin[1] = nums[i]
      else:
        xmin[0] = nums[i]
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2,3,4,5],
    [1,1,1,1,1],
    [5,4,3,2,1],
    [5,1,4,2,3],
    [3,2,5,1,4]
  ]
  rslts = [solver.increasingTriplet(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")