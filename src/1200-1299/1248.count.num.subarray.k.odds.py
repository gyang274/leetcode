from typing import List

class Solution:
  def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    nums = list(map(lambda x: x & 1, nums))
    i, j, s, m, n = 0, 0, 0, 0, len(nums)
    while i < n:
      while j < n and s < k:
        s += nums[j]
        j += 1
      if s == k:
        r = 1
        while j < n and nums[j] == 0:
          j += 1
          r += 1
        l = 1
        while i < n and nums[i] == 0:
          i += 1
          l += 1
        m += l * r
      s -= nums[i]
      i += 1
    return m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,3,5], 1),
    ([2,4,6], 1),
    ([1,1,2,1,1], 2),
    ([1,1,2,1,1], 3),
    ([2,2,2,1,2,2,1,2,2,2], 2),
  ]
  rslts = [solver.numberOfSubarrays(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
