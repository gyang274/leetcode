from typing import List

class Solution:
  def specialArray(self, nums: List[int]) -> int:
    # TC: O(NlogN), sort, SC: O(1), refr. H-index.
    nums.sort(reverse=True)
    i = 0
    while i < len(nums) and nums[i] > i:
      i += 1
    return -1 if i < len(nums) and i == nums[i] else i

class Solution:
  def specialArray(self, nums: List[int]) -> int:
    # TC: O(NlogN), sort, SC: O(1), refr. H-index.
    nums.sort(reverse=True)
    l, r = 0, len(nums)
    while l < r:
      m = l + (r - l) // 2
      if m >= nums[m]:
        r = m
      else:
        l = m + 1
    return -1 if l < len(nums) and l == nums[l] else l

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [3,5],
    [1,3,5],
    [0,4,3,0,4],
  ]
  rslts = [solver.specialArray(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
