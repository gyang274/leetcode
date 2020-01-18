from typing import List


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    i = 0
    j = n - 1
    while i <= j:
      k = (i + j) // 2
      if nums[k] == target:
        return k
      # left half i -> k is sorted
      if nums[i] <= nums[k]:
        if nums[i] <= target and target < nums[k]:
          j = k - 1
        else:
          i = k + 1
      # right half k -> j is sorted
      else:
        if nums[k] < target and target <= nums[j]: 
          i = k + 1
        else:
          j = k - 1
    return -1


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([4,5,6,7,0,1,2],  0),
    ([4,5,6,7,0,1,2], -1),
  ]
  rslts = [solver.search(nums, target) for nums, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
