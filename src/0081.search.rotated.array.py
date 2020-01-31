from typing import List


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    """This is same as 0033 except possible duplicate in nums. How duplicate impact?
      For example, [3, 0, 1, 2, 3, 3, 3, 3, 3], nums[lft] == nums[mid] == num[rgt],
      in this case, don't where to move, so shrink both side lft += 1 and rgt -= 1,
      so worst case O(n).
    """
    n = len(nums)
    i = 0
    j = n - 1
    while i <= j:
      k = (i + j) // 2
      if nums[k] == target:
        return True
      if nums[i] == nums[k] == nums[j]:
        i += 1
        j -= 1
      else:
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
    return False


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([2,5,6,0,0,1,2], 0),
    ([2,5,6,0,0,1,2], 3),
    ([3, 0, 1, 2, 3, 3, 3, 3, 3], 3),
    ([3, 0, 1, 2, 3, 3, 3, 3, 3], 0),
    ([3, 4, 1, 2, 3, 3, 3, 3, 3], 4),
    ([3, 4, 1, 2, 3, 3, 3, 3, 3], 2),
  ]
  rslts = [solver.search(nums, target) for nums, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")