class Solution:
  def isPalindrome(self, N: int) -> bool:
    s = str(N)
    n = len(s)
    if n & 1:
      x, m, y = s[:(n // 2)], s[n // 2], s[(n // 2 + 1):]
    else:
      x, y = s[:(n // 2)], s[(n // 2):]
    return x[::-1] == y
  def nextPalindrome(self, N: int) -> int:
    s = str(N)
    n = len(s)
    if n & 1:
      x, m, y = s[:(n // 2)], s[n // 2], s[(n // 2 + 1):]
      if x[::-1] > y:
        return int(x + m + x[::-1])
      elif m < '9':
        return int(x + str(int(m) + 1) + x[::-1])
      elif x < '9' * (n // 2):
        return int(str(int(x) + 1) + '0' + str(int(x) + 1)[::-1])
      else:
        return int('1' + '0' * (n - 1) + '1')
    else:
      x, y = s[:(n // 2)], s[(n // 2):]
      if x[::-1] > y:
        return int(x + x[::-1])
      elif x < '9' * (n // 2):
        return int(str(int(x) + 1) + str(int(x) + 1)[::-1])
      else:
        return int('1' + '0' * (n - 1) + '1')
  def superpalindromesInRange(self, L: str, R: str) -> int:
    L, R = int(L), int(R)
    # init
    x = int(L ** 0.5)
    x = x if self.isPalindrome(x) else self.nextPalindrome(x)
    while x ** 2 < L:
      x = self.nextPalindrome(x)
    # main
    ans = []
    while x ** 2 <= R:
      if self.isPalindrome(x ** 2):
        ans.append(x ** 2)
      x = self.nextPalindrome(x)
    return len(ans)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("4", "1000"),
  ]
  rslts = [solver.superpalindromesInRange(L, R) for L, R in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
