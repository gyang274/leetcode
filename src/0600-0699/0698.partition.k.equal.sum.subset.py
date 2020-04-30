from typing import List

class Solution:
  def backtrack(self, x, nums):
    key = tuple(nums)
    if key not in self.memo:
      if x == 0 and sum(nums) == self.t:
        self.memo[key] = True
      else:
        self.memo[key] = False
        for i in range(len(nums)):
          if x + nums[i] <= self.t:
            numsnext = nums.copy()
            if self.backtrack((x + numsnext.pop(i)) % self.t, numsnext):
              self.memo[key] = True
              break
    return self.memo[key]
  def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    xsum = sum(nums)
    if xsum % k or max(nums) > xsum // k:
      return False
    # target
    self.memo, self.t = {}, xsum // k
    nums.sort(reverse=True)
    return self.backtrack(0, nums)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,2,2], 2),
    ([2,3,5,1,4], 3),
    ([1,1,1,1,4,4,4,4], 4),
    ([10,10,10,7,7,7,7,7,7,6,6,6], 3),
  ]
  rslts = [solver.canPartitionKSubsets(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
