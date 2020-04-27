import math

class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0:
      return False
    p = x
    q = 0
    while p > 9:
      q *= 10
      q += p % 10
      p //= 10
    return q == x // 10 and p == x % 10

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    121, -121, 10201, 11, 1221, 10, 0, 1, 1000021,
  ]
  rslts = [solver.isPalindrome(x) for x in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
