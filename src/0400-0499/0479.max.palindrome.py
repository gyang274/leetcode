import math

class Solution:
  def largestPalindrome(self, n: int) -> int:
    """brute-force
    """
    if n == 1:
      return 9
    upper = 10 ** n - 1
    lower = 10 ** (n - 1)
    for i in range(upper, lower - 1, -1):
      p = int(str(i) + str(i)[::-1])
      x = upper
      while x * x >= p:
        if p % x == 0 and len(str(p // x)) == n:
          return p % 1337
        x -= 1
    return None

class Solution:
  def largestPalindrome(self, n: int) -> int:
    # math
    # suppose palindrome = 10^n * L + R = (10^n - x)*(10^n - y), R = L[::-1]
    # suppose L = 10^n - z
    # 10^n * (x + y - z) = x * y - R
    # suppose x + y < 10^n and x * y < 10^n (=> why n <= 8)
    # z = x + y, R = x * y
    # R = x(z - x)
    # x^2 - xz + R = 0
    # x = z +- sqrt(z^2 - 4R) / 2 is integer
    if n == 1:
      return 9
    bound = 10 ** n
    upper = bound - 1
    lower = bound // 10
    for L in range(upper, lower - 1, -1):
      z, R = bound - L, int(str(L)[::-1])
      d = z * z - 4 * R
      if d >= 0 and int(math.sqrt(d)) ** 2 == d:
        # R losts leading 0s
        return int(str(L) + str(L)[::-1]) % 1337
    return None

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 4, 5, 6, 7, 8,
  ]
  rslts = [solver.largestPalindrome(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")