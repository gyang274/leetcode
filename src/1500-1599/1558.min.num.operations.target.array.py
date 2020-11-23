from typing import List

class Solution:
  def minOperations(self, nums: List[int]) -> int:
    # TC: O(NlogM), SC: O(1), n = len(nums), m = max(nums)
    def numOperations(x):
      # TC: O(logX)
      n1, n2 = 0, 0
      while x:
        if x & 1:
          n1 += 1
          x -= 1
        else:
          n2 += 1
          x >>= 1
      return n1, n2
    # operation -1 is self, //2 is shared.
    n1, n2 = 0, 0
    for x in nums:
      x1, x2 = numOperations(x)
      n1 += x1
      n2 = max(n2, x2)
    return n1 + n2

class Solution:
  def minOperations(self, nums: List[int]) -> int:
    return sum(bin(x).count('1') for x in nums) + len(bin(max(nums))) - 3

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2,3,4,5],
    [1,3,5,7,9,11],
    [2,4,6,8,16,32],
  ]
  rslts = [solver.minOperations(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
