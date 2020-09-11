from typing import List

class Solution:
  def getGCD(self, x: int, y: int) -> int:
    while y:
      x, y = y, x % y
    return x  
  def getLCM(self, x: int, y: int) -> int:
    return x * y // self.getGCD(x, y)
  def isGoodArray(self, nums: List[int]) -> bool:
    # question is equivalent to have any substr with gcd equals 1, iff array has gcd equals to 1
    n = len(nums)
    x, i = nums[0], 1
    while i < n:
      x = self.getGCD(x, nums[i])
      if x == 1:
        return True
      i += 1
    return x == 1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [12,5,7,23],
  ]
  rslts = [solver.isGoodArray(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
