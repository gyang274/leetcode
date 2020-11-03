from typing import List

class Solution:
  def minSubsequence(self, nums: List[int]) -> List[int]:
    s, ans, x, nums = 0, [], sum(nums) // 2, sorted(nums)
    while s <= x:
      s += nums[-1]
      ans.append(nums.pop())
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.minSubsequence(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
