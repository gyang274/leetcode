from typing import List


class Solution:
  def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    rslt = []
    for i in range(len(nums) - 3):
      if i > 0 and nums[i] == nums[i-1]:
        continue
      for j in range(i + 1, len(nums) - 2):
        if j > (i + 1) and nums[j] == nums[j-1]:
          continue
        s = target - nums[i] - nums[j]
        k = j + 1
        l = len(nums) - 1
        while k < l:
          nkl = nums[k] + nums[l]
          if nkl == s:
            rslt.append([nums[i], nums[j], nums[k], nums[l]])
            k += 1
            while k < l and nums[k] == nums[k - 1]:
              k += 1
            l -= 1
            while l > k and nums[l] == nums[l + 1]:
              l -= 1
          if nkl < s:
            k += 1
            while k < l and nums[k] == nums[k - 1]:
              k += 1
          else:
            l -= 1
            while l > k and nums[l] == nums[l + 1]:
              l -= 1
    return rslt


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([1, 0, -1, 0, -2, 2], 0),
    ([0, 0, 0, 0], 0),
    ([0, 0, 0, 0, 0, 0, 0], 0)
  ]
  rslts = [solver.fourSum(nums, target) for nums, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"cases: {cs} | solution: {rs}")