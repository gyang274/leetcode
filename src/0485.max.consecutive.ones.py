from typing import List

class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
      return 0
    for i in range(n):
      if i > 0 and nums[i] == 1:
        nums[i] += nums[i - 1]
    return max(nums)

class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    n1max, n1 = 0, 0
    for x in nums:
      if x == 0:
        n1 = 0
      else:
        n1 += 1
        n1max = max(n1max, n1)
    return n1max

class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    return max(map(len, ''.join(map(str, nums)).split('0')))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [1,0,1,1],
  ]
  rslts = [solver.findMaxConsecutiveOnes(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  