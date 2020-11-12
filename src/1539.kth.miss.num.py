from typing import List

class Solution:
  def findKthPositive(self, nums: List[int], k: int) -> int:
    n = len(nums)
    i, m = 0, 0
    for x in range(1, 2048):
      if i < n and x == nums[i]:
        i += 1
      else:
        m += 1
        if m == k:
          return x
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,4], 2),
    ([2,3,4,7,11], 5),
  ]
  rslts = [solver.findKthPositive(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
