from typing import List

class Solution:
  def singleNonDuplicate(self, nums: List[int]) -> int:
    # modified binary search
    l, r = 0, len(nums) - 1
    while l < r:
      k = (r - l) // 2
      m = l + k
      if nums[m] == nums[m - 1]:
        if k & 1:
          l = m + 1
        else:
          r = m - 2
      elif nums[m] == nums[m + 1]:
        if k & 1:
          r = m - 1
        else:
          l = m + 2
      else:
        return nums[m]
    return nums[l]

class Solution:
  def singleNonDuplicate(self, nums: List[int]) -> int:
    # modified binary search
    # search over even index only, O(log(N/2)) ~= O(logN)
    l, r = 0, len(nums) // 2
    while l < r:
      m = l + (r - l) // 2
      if nums[2 * m] == nums[2 * m + 1]:
        l = m + 1
      elif nums[2 * m] == nums[2 * m - 1]:
        r = m - 1
      else:
        return nums[2 * m]
    return nums[2 * l]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,1,2],
    [1,2,2],
    [1,1,2,2,3,5,5],
  ]
  rslts = [solver.singleNonDuplicate(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
