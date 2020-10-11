from typing import List

class Solution:
  def sumFourDivisorsInt(self, x):
    if x < 6:
      return 0
    count, ans = 2, 1 + x
    for d in range(2, int(x ** 0.5) + 1):
      if x % d == 0:
        if d < x // d:
          count += 2
          ans += d + x // d
        elif d == x // d:
          count += 1
          ans += d
        if count > 4:
          return 0
    return ans if count == 4 else 0
  def sumFourDivisors(self, nums: List[int]) -> int:
    return sum(map(self.sumFourDivisorsInt, nums))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,5,8,21],
  ]
  rslts = [solver.sumFourDivisors(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")