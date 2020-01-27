from typing import List


class Solution:
  def canJump(self, nums: List[int]) -> bool:
    """Dynamic Programming: O(n^2).
    """
    n = len(nums)
    nums[n - 1] = True
    for i in range(n - 2, -1, -1):
      nums[i] = any(nums[(i + 1):(i + nums[i] + 1)])
    return nums[0]


class Solution:
  def canJump(self, nums: List[int]) -> bool:
    """Greedy Approach: O(n).
      Key observation: as long as i + nums[i] >= k, where k is the smallest index can reach to the end. 
    """
    n = len(nums)
    k = n - 1
    for i in range(n - 1, -1, -1):
      nums[i], k = (True, i) if i + nums[i] >= k else (False, k)
    return nums[0]


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.canJump(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  
