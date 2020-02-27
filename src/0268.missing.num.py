from typing import List

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    i, n = 0, len(nums)
    while i < n:
      if i == nums[i] or nums[i] == n:
        i += 1
      else:
        j = nums[i]
        nums[i] , nums[j] = nums[j], nums[i]
    for i in range(n):
      if nums[i] == n:
        return i
    return n

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    """Q0136: inspired by Q0136.
    """
    x, n = 0, len(nums)
    for i in range(n):
      x ^= (i ^ nums[i])
    return x ^ n

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    return len(nums) * (len(nums) + 1) // 2 - sum(nums)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [0],
    [1],
    [0,1,2],
    [3,1,0],
    [9,6,7,2,3,5,8,0,1],
  ]
  rslts = [solver.missingNumber(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")