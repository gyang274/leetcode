from typing import List

class Solution:
  def findErrorNums(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0, 0]
    i = 0
    while i < n:
      if nums[i] == i + 1:
        i += 1
      else:
        j = nums[i] - 1
        if nums[i] == nums[j]:
          ans[0] = nums[i]
          break
        else:
          nums[i], nums[j] = nums[j], nums[i]
    ans[1] = n * (n + 1) // 2 + ans[0] - sum(nums)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,1],
    [1,1,2,3,4,5,6],
    [4,3,2,7,8,2,3,1],
  ]
  rslts = [solver.findErrorNums(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
