from typing import List

class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    """Sort: O(NlogN), Switch along the way: O(N).
      Q0142: Floyd's Tortoise and Hare - Cycle Detection: O(N).
    """
    i, n = 0, len(nums)
    # nums contains 1, .., n - 1, so if nums[i] = i + 1, then nums[n - 1] is the repeated one.
    # else if nums[i] = j and nums[j] = j, then found repeated one before reaching to the end.
    while i < n - 1:
      if nums[i] == i + 1:
        i += 1
      else:
        j = nums[i] - 1
        if nums[i] == nums[j]:
          return nums[i]
        else:
          nums[i], nums[j] = nums[j], nums[i]
    return nums[n - 1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,3,4,2,1],
    [1,3,4,2,2],
    [3,1,3,4,2],
    [4,1,2,2,2],
  ]
  rslts = [solver.findDuplicate(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
        