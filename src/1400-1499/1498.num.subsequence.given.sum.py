from typing import List

class Solution:
  def numSubseq(self, nums: List[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    i, j, count = 0, n - 1, 0
    while i <= j:
      while i <= j and nums[i] + nums[j] > target:
        j -= 1
      if i <= j:
        # nums[i] be the min, any combinations of nums[(i+1):(j+1)]
        count += 1 << (j - i)
      i += 1
    return count % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,3,4,6,7], 12),
  ]
  rslts = [solver.numSubseq(nums, target) for nums, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
