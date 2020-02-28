from typing import List


class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    i = 0
    j = n - 1
    ok = False
    while i <= j:
      k = (i + j) // 2
      if nums[k] > target:
        j = k - 1
      elif nums[k] < target:
        i = k + 1
      else:
        ok = True
        break
    if ok:
      kk = k
      while i < k:
        m = (i + k) // 2
        if nums[m] < target:
          i = m + 1
        else:
          k = m
      k = kk
      while k < j:
        m = (k + j + 1) // 2
        if nums[m] > target:
          j = m - 1
        else:
          k = m
    else:
      return [-1, -1]
    return [i, j]


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([], 0),
    ([5, 7, 7, 8, 8, 10], 5),
    ([5, 7, 7, 8, 8, 10], 8),
    ([5, 7, 7, 8, 8, 10], 6),
  ]
  rslts = [solver.searchRange(nums, target) for nums, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")