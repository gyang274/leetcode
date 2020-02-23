from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    """O(N), product from left and from product right.
    """
    l, r = [1] * len(nums), [1] * len(nums)
    for i in range(1, len(nums)):
      l[i] = l[i - 1] * nums[i - 1]
    for i in range(len(nums) - 2, -1, -1):
      r[i] = r[i + 1] * nums[i + 1]
    return [x * y for x, y in zip(l, r)]

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    """TC: O(N), SC: O(1), product from left and from product right, use output in-place
    """
    ans = [1] * len(nums)
    for i in range(1, len(nums)):
      ans[i] = ans[i - 1] * nums[i - 1]
    hold = 1
    for i in range(len(nums) - 2, -1, -1):
      hold *= nums[i + 1]
      ans[i] *= hold
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2,3,4],
  ]
  rslts = [solver.productExceptSelf(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")