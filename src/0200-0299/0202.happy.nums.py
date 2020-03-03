class Solution:
  def powerUp(self, n: int) -> int:
    ans = 0
    while n > 0:
      ans += (n % 10) ** 2
      n //= 10
    return ans
  def isHappy(self, n: int) -> bool:
    seen = set()
    while n not in seen:
      seen.add(n)
      n = self.powerUp(n)
      if n == 1:
        return True
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0,
    1,
    2,
    3,
    5,
    9,
    19,
    42,
    81,
    99,
    162,
    999,
    243,
    324,
    9999,
  ]
  rslts = [solver.isHappy(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}") 