from typing import List

class Solution:
  def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
    if a == 0:
      if b >= 0:
        vals = nums
      else:
        vals = nums[::-1]
    else:
      # reflection point -b/(2a)
      z = -1 * b / (2 * a)
      # binary search the split position i, such that nums[i-1] < z <= nums[i]
      l, r = 0, len(nums)
      while l < r:
        m = l + (r - l) // 2
        if z <= nums[m]:
          r = m
        else:
          l = m + 1
      # sort nums w.r.t abs dist to z
      i, j, k, vals = l - 1, l, 0, [None] * len(nums)
      while i > -1 or j < len(nums):
        if i == -1:
          vals[k] = nums[j]
          j += 1
        elif j == len(nums):
          vals[k] = nums[i]
          i -= 1
        elif abs(nums[i] - z) <= abs(nums[j] - z):
          vals[k] = nums[i]
          i -= 1
        else:
          vals[k] = nums[j]
          j += 1
        k += 1
      if a < 0:
        vals = vals[::-1]
    return [a * (x ** 2) + b * x + c for x in vals]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([-4,-2,2,4],  0,  0, 1),
    ([-4,-2,2,4],  0,  1, 2),
    ([-4,-2,2,4],  0, -2, 3),
    ([-4,-2,2,4],  2,  3, 5),
    ([-4,-2,2,4], -2,  3, 5),
    ([-4,-2,2,4], -2, -3, 5),
  ]
  rslts = [solver.sortTransformedArray(nums, a, b, c) for nums, a, b, c in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
